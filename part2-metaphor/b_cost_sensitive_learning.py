# %% [markdown]
# # Notebook B: cost-sensitive learning
#
# A classifier does not decide, on its own, how bad a false positive is compared
# to a false negative. A person picks that. That choice, the cost matrix, is a
# moral statement wearing a technical costume.
#
# This notebook shows the same model, the same data, three different cost
# matrices, and three different behaviors. Then it asks: who is being charged for
# each kind of mistake, and did anyone consent to that.

# %% [markdown]
# ## Reflection
#
# The model does not decide how bad a false positive is. A person sets that in
# the cost matrix, and then the whole system runs on it. Change the matrix and
# you change what the system is willing to do to people. It is a moral statement
# wearing a technical costume. In the atonement the cost of the wrong was not set
# low and it was not negotiated. It was paid in full, by someone who was not the
# offender. There is a difference between saying this sin is cheap and saying the
# full price was paid for you. The first is a discount. The second is a gift. The
# cost matrix is where you find out which one a system actually believes.

# %%
import numpy as np
from sklearn.linear_model import LogisticRegression

rng = np.random.default_rng(26)

# %% [markdown]
# ## Synthetic cases
#
# Two groups of people, a feature that is genuinely predictive, and a true label.
# Nothing here is a real person. The label is abstract: 1 means "the thing the
# system is trying to catch happened".

# %%
n = 2000
feat = rng.normal(0, 1, n)
logit = 0.9 * feat - 0.3
p_true = 1 / (1 + np.exp(-logit))
y = (rng.uniform(size=n) < p_true).astype(int)

X = feat.reshape(-1, 1)
model = LogisticRegression().fit(X, y)
scores = model.predict_proba(X)[:, 1]

print(f"base rate of positives: {y.mean():.3f}")

# %% [markdown]
# ## Three cost matrices
#
# We pick the decision threshold that minimizes expected cost for each matrix.
# fp = predicted 1, truth 0 (a wrongful flag). fn = predicted 0, truth 1 (a
# missed case).

# %%
def confusion_at(threshold):
    pred = (scores >= threshold).astype(int)
    tp = int(((pred == 1) & (y == 1)).sum())
    fp = int(((pred == 1) & (y == 0)).sum())
    tn = int(((pred == 0) & (y == 0)).sum())
    fn = int(((pred == 0) & (y == 1)).sum())
    return tp, fp, tn, fn

def best_threshold(cost_fp, cost_fn):
    grid = np.linspace(0.01, 0.99, 99)
    costs = []
    for t in grid:
        _, fp, _, fn = confusion_at(t)
        costs.append(fp * cost_fp + fn * cost_fn)
    i = int(np.argmin(costs))
    return grid[i], costs[i]

matrices = {
    "symmetric (fp=1, fn=1)":            (1, 1),
    "protect the innocent (fp=5, fn=1)": (5, 1),
    "catch every case (fp=1, fn=5)":     (1, 5),
}

for name, (cfp, cfn) in matrices.items():
    t, total = best_threshold(cfp, cfn)
    tp, fp, tn, fn = confusion_at(t)
    print(f"\n{name}")
    print(f"  chosen threshold: {t:.2f}")
    print(f"  flags raised: {tp + fp:>4}   wrongful flags (fp): {fp:>4}   missed (fn): {fn:>4}")
    print(f"  total cost under its own matrix: {total}")

# %% [markdown]
# ## The point
#
# The "protect the innocent" matrix raises fewer flags and misses more real
# cases. The "catch every case" matrix does the reverse. Neither is more
# accurate. They encode different answers to "what is worse".
#
# Notice what the symmetric matrix hides: calling fp and fn equal is still a
# choice, and it is usually the wrong one. Someone always pays for the missed
# cases and the wrongful flags. The cost matrix just decides who, quietly.

# %%
# A weak guard so the notebook fails loudly if the data stops behaving.
t_sym, _ = best_threshold(1, 1)
t_prot, _ = best_threshold(5, 1)
assert t_prot > t_sym, "raising the fp cost should raise the threshold"
print("\nPASS: charging more for wrongful flags made the model slower to flag.")

# %% [markdown]
# ## Where this points
#
# Cost-sensitive learning conserves cost in the accounting sense: the matrix
# names a price and the optimizer respects it. What it never does is pay the
# price itself. It distributes the bill. Notebook C is about a payer who does not
# distribute it.
