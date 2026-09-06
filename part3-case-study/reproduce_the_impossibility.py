# %% [markdown]
# # Part 3: reproducing the fairness impossibility result
#
# This notebook does not build anything. It loads a public dataset behind an
# already-published analysis (ProPublica, 2016) and re-derives a result that
# ProPublica, then Chouldechova (2017), then Kleinberg, Mullainathan and
# Raghavan (2016) all published: when two groups have different base rates for an
# outcome, a risk score cannot be equally calibrated across the groups and also
# give them equal false positive and false negative rates. You get to pick which
# one to equalize. You cannot have both.
#
# The theological reading is in `reading.md`. That prose is yours to write.
#
# ## What this notebook will not do
#
# No model is trained. No score is produced. No threshold is tuned toward
# leniency. Everything below is descriptive statistics on published data.

# %%
from pathlib import Path
import sys
import numpy as np
import pandas as pd

DATA = Path("data/compas-scores-two-years.csv")
if not DATA.exists():
    sys.exit(
        "Missing data/compas-scores-two-years.csv. "
        "See data/README.md for the one-line curl command to fetch it."
    )

df = pd.read_csv(DATA)
print(f"raw rows: {len(df)}")

# %% [markdown]
# ## ProPublica's filtering
#
# These are the exact filters from ProPublica's published notebook. They keep
# cases where the arrest and the COMPAS screening line up in time and the record
# is complete.

# %%
df = df[
    (df["days_b_screening_arrest"] <= 30)
    & (df["days_b_screening_arrest"] >= -30)
    & (df["is_recid"] != -1)
    & (df["c_charge_degree"] != "O")
    & (df["score_text"] != "N/A")
].copy()
print(f"rows after ProPublica filters: {len(df)}")

# Restrict to the two groups the published analysis compares.
df = df[df["race"].isin(["African-American", "Caucasian"])].copy()
df["group"] = df["race"].map(
    {"African-American": "Black defendants", "Caucasian": "White defendants"}
)

# COMPAS "high or medium" vs "low". This is the operational cut ProPublica used.
df["high_risk"] = (df["score_text"] != "Low").astype(int)
df["reoffended"] = df["two_year_recid"].astype(int)

# %% [markdown]
# ## Base rates differ
#
# This is the fact that drives everything else. It is not created by the
# algorithm. It is in the data the algorithm was asked to predict.

# %%
base = df.groupby("group")["reoffended"].mean()
print(base.round(3).to_string())

# %% [markdown]
# ## Calibration: is a given score level about equally predictive per group
#
# For each COMPAS decile, what fraction actually reoffended. If the lines track
# each other, the score is calibrated across groups.

# %%
calib = (
    df.groupby(["group", "decile_score"])["reoffended"]
    .mean()
    .unstack("group")
)
print(calib.round(2).to_string())
print(
    "\nThe two columns are close at most score levels. COMPAS is roughly "
    "calibrated by group. This is what Northpointe pointed to in their rebuttal."
)

# %% [markdown]
# ## Error rates: the ProPublica finding
#
# Using high_risk as the prediction and reoffended as the truth.

# %%
def rates(sub):
    y = sub["reoffended"].values
    p = sub["high_risk"].values
    fp = int(((p == 1) & (y == 0)).sum())
    fn = int(((p == 0) & (y == 1)).sum())
    neg = int((y == 0).sum())
    pos = int((y == 1).sum())
    return pd.Series({
        "false_positive_rate": fp / neg,
        "false_negative_rate": fn / pos,
        "n": len(sub),
    })

err = df.groupby("group").apply(rates, include_groups=False)
print(err.round(3).to_string())

print(
    "\nProPublica reported roughly: false positive rate around 0.45 for Black "
    "defendants vs around 0.23 for white defendants, and false negative rate "
    "around 0.28 vs around 0.48. Your numbers should land near those."
)

# %% [markdown]
# ## The tradeoff, stated as the theorem
#
# Chouldechova (2017): if base rates differ between groups and a score is
# calibrated across them, then the groups must have different false positive
# rates and different false negative rates. The gap you see above is not a tuning
# mistake. It is forced by the arithmetic the moment you require calibration and
# the base rates are unequal.

# %%
bp = base["Black defendants"]
wp = base["White defendants"]
assert abs(bp - wp) > 0.05, "expected a visible base rate gap between groups"

fpr_gap = err.loc["Black defendants", "false_positive_rate"] - err.loc[
    "White defendants", "false_positive_rate"
]
assert fpr_gap > 0.1, (
    "expected a large false-positive-rate gap, matching the published finding"
)
print(f"PASS: base rate gap = {abs(bp - wp):.3f}")
print(f"PASS: false positive rate gap = {fpr_gap:.3f} (published: about 0.22)")

# %% [markdown]
# ## Hand-off to the reading
#
# Numbers established, go write `reading.md`. The mapping to work from:
#
# - a false positive here is a person labeled a future danger who was not:
#   wrongful condemnation
# - the base rate gap is harm that entered the data upstream of the model:
#   something inherited, not chosen by the people being scored
# - the decision threshold is where a system can be made more lenient, and also
#   where accountability quietly leaks: leniency is not the same as grace
# - a system that only sorts people into risk bins does nothing to restore any of
#   them: retributive prediction cannot produce reconciliation
#
# And the hard line for the essay: this is why the repo does not build a
# "grace-adjusted" version of this score. You cannot fix a sorting machine by
# making it sort more kindly.
