# %% [markdown]
# # Notebook D: calibration
#
# Romans 3:26 says God is "just and the justifier". Not just, and then separately
# merciful. Just in the act of justifying. The judgment is merciful and it is
# also true.
#
# Calibration is the closest technical shadow of that "and". A calibrated model
# is one whose stated confidence matches reality: of all the cases it calls 70
# percent likely, about 70 percent actually are. A model can be accurate and
# still lie about its confidence. A model can be well calibrated overall and
# still be unfair across groups. This notebook shows both, and sets up Part 3.

# %% [markdown]
# ## Reflection
#
# A lenient judge and a truthful judge are not the same thing. A model that says
# not guilty more often than the facts warrant is not merciful, it is
# miscalibrated. It is wrong in a direction we happen to like. Cheap grace works
# the same way. It lowers the verdict instead of dealing with it. The cross is
# not a soft verdict. It is a true reckoning, the full weight named correctly,
# and then absorbed by a substitute. Calibration is just the technical word for
# telling the truth about what you see. Grace never asked anyone to stop telling
# the truth. It asked someone to carry what the truth cost.

# %%
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.calibration import calibration_curve
from sklearn.metrics import brier_score_loss
import matplotlib.pyplot as plt

rng = np.random.default_rng(26)

# %% [markdown]
# ## Two groups with different base rates
#
# This is the setup that makes Part 3's impossibility result unavoidable. Group A
# and Group B have genuinely different base rates for the outcome. Everything
# else about the model is the same.

# %%
n = 4000
group = rng.integers(0, 2, n)          # 0 = A, 1 = B
feat = rng.normal(0, 1, n)
# Group B has a higher base rate, built into the intercept.
logit = 1.0 * feat - 0.6 + 0.9 * group
p_true = 1 / (1 + np.exp(-logit))
y = (rng.uniform(size=n) < p_true).astype(int)

X = np.column_stack([feat, group])
model = LogisticRegression().fit(X, y)
scores = model.predict_proba(X)[:, 1]

for g, name in [(0, "A"), (1, "B")]:
    m = group == g
    print(f"group {name}: base rate {y[m].mean():.3f}, "
          f"mean predicted {scores[m].mean():.3f}, "
          f"Brier {brier_score_loss(y[m], scores[m]):.3f}")

# %% [markdown]
# ## Reliability: is the confidence honest

# %%
fig, ax = plt.subplots(figsize=(5.5, 5.5))
ax.plot([0, 1], [0, 1], color="grey", ls="--", label="perfectly calibrated")
for g, name in [(0, "A"), (1, "B")]:
    m = group == g
    frac_pos, mean_pred = calibration_curve(y[m], scores[m], n_bins=8, strategy="quantile")
    ax.plot(mean_pred, frac_pos, marker="o", label=f"group {name}")
ax.set_xlabel("model's stated probability")
ax.set_ylabel("actual fraction positive")
ax.set_title("does the model mean what it says")
ax.legend()
fig.tight_layout()
fig.savefig("part2-metaphor/figures/d_reliability.png", dpi=110)
print("saved part2-metaphor/figures/d_reliability.png")

# %% [markdown]
# ## A single threshold, two error profiles

# %%
THRESH = 0.5
pred = (scores >= THRESH).astype(int)
for g, name in [(0, "A"), (1, "B")]:
    m = group == g
    fp = int(((pred == 1) & (y == 0) & m).sum())
    fn = int(((pred == 0) & (y == 1) & m).sum())
    pos = int(m.sum())
    print(f"group {name}: false positive rate {fp / max((y[m] == 0).sum(), 1):.3f}, "
          f"false negative rate {fn / max((y[m] == 1).sum(), 1):.3f}")

print("\nSame model, same threshold. The two groups do not get the same error"
      " rates, because their base rates differ. Part 3 shows this is not a bug"
      " you can tune away. It is a theorem.")

# %%
fpr = {}
for g in (0, 1):
    m = group == g
    fpr[g] = int(((pred == 1) & (y == 0) & m).sum()) / max(int(((y == 0) & m).sum()), 1)
assert abs(fpr[0] - fpr[1]) > 0.02, (
    "expected the two groups to have visibly different false positive rates"
)
print("PASS: one honest model still produces unequal error rates across groups.")

# %% [markdown]
# ## Where this points
#
# Calibration is what keeps grace from collapsing into denial. A true judgment
# can still be absorbed by a substitute. A false judgment absorbs nothing,
# because there was nothing really there to carry. Part 1 essay 02 makes this
# argument in words.
#
# Part 3 takes the group gap above and shows it is mathematically forced.
