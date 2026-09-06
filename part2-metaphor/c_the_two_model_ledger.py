# %% [markdown]
# # Notebook C: the two-model ledger
#
# **The centerpiece.** Standard library only. No numpy, no sklearn.
#
# The claim from Part 1: substitution *conserves* the cost. The full penalty is
# still paid. Only the payer changes.
#
# This notebook builds the smallest honest picture of that. Model A makes
# predictions, gets some wrong, and each wrong answer carries a real cost. Those
# costs accumulate into a debt. Then Model B absorbs the entire debt. We show two
# things at the end, by assertion, not by eyeballing:
#
# 1. Model A's ledger goes to zero.
# 2. The total on the books is exactly what it was. Nothing shrank. It moved.
#
# Read `where-the-analogy-breaks.md` before you take this too far. ML has no
# native substitution step. We are building the shape by hand.

# %% [markdown]
# ## Reflection
#
# The cheap version of grace is the one where the debt quietly gets smaller.
# Nobody paid it, it just shrank. This notebook does not let that happen. The
# number that leaves Model A arrives whole at Model B. The total on the books
# does not move. That is the whole point. Grace that costs nobody anything is not
# grace, it is forgetting. What it costs Model B is that it now carries the full
# debt it did not run up, and its own record only looks clean because someone
# moved the weight, not because the weight was light. Christ is the one holding
# the weight. The books balanced because He carried them.

# %%
import random
import matplotlib.pyplot as plt

random.seed(26)

# %% [markdown]
# ## A tiny world
#
# 40 cases. Each has a true label: 1 means "guilty of the thing", 0 means "not".
# Model A predicts each one. Every mistake has a price set by the cost matrix.

# %%
N = 40
truth = [1 if random.random() < 0.45 else 0 for _ in range(N)]

# Model A is decent but not perfect: it flips the true label with some probability.
def model_a_predict(y_true, flip_prob=0.25):
    return [1 - y if random.random() < flip_prob else y for y in y_true]

pred_a = model_a_predict(truth)

# Cost matrix. A false positive (condemn the innocent) costs more than a false
# negative here. That asymmetry is a moral choice, not a technical one. See
# Notebook B.
COST = {
    ("fp", ): 5,   # predicted 1, truth 0
    ("fn", ): 3,   # predicted 0, truth 1
}

def error_kind(y_true, y_pred):
    if y_pred == 1 and y_true == 0:
        return "fp"
    if y_pred == 0 and y_true == 1:
        return "fn"
    return None

# %% [markdown]
# ## Model A runs up a debt

# %%
ledger_a = []  # one entry per mistake: (case_index, kind, cost)
for i, (yt, yp) in enumerate(zip(truth, pred_a)):
    kind = error_kind(yt, yp)
    if kind is not None:
        ledger_a.append((i, kind, COST[(kind,)]))

debt_a = sum(cost for _, _, cost in ledger_a)

print(f"Model A made {len(ledger_a)} mistakes across {N} cases.")
print(f"Model A's debt: {debt_a}")
for i, kind, cost in ledger_a:
    print(f"  case {i:>2}  {kind}  cost {cost}")

books_total_before = debt_a
print(f"\nTotal on the books before substitution: {books_total_before}")

# %% [markdown]
# ## Substitution
#
# Model B does not fix Model A's predictions. It does not lower the cost matrix.
# It does not argue that the mistakes were smaller than they were. It takes the
# debt onto itself, in full.

# %%
ledger_b = []          # what B now holds
for entry in ledger_a:
    ledger_b.append(entry)   # transferred as-is, same cost, same case

debt_b = sum(cost for _, _, cost in ledger_b)

# A's ledger is cleared. Not erased from history: the mistakes still happened and
# are still listed above. But A no longer owes anything.
ledger_a_after = []
debt_a_after = sum(cost for _, _, cost in ledger_a_after)

books_total_after = debt_a_after + debt_b

print(f"Model A's debt after substitution: {debt_a_after}")
print(f"Model B now holds:                 {debt_b}")
print(f"Total on the books after:          {books_total_after}")

# %% [markdown]
# ## The two things this notebook exists to show

# %%
assert debt_a_after == 0, "Model A's ledger did not clear"
assert books_total_after == books_total_before, (
    f"the total changed: {books_total_before} -> {books_total_after}"
)
assert debt_b == books_total_before, "Model B is not holding the full amount"

print("PASS: Model A's ledger is zero.")
print("PASS: the total on the books is unchanged.")
print(f"PASS: Model B carries the whole {debt_b}, exactly what A owed.")

# %% [markdown]
# ## The picture

# %%
fig, ax = plt.subplots(figsize=(7, 4.5))
labels = ["before", "after"]
x = range(len(labels))
width = 0.35

a_vals = [books_total_before, debt_a_after]
b_vals = [0, debt_b]

ax.bar([i - width / 2 for i in x], a_vals, width, label="Model A", color="#4c72b0")
ax.bar([i + width / 2 for i in x], b_vals, width, label="Model B", color="#dd8452")

for i, v in enumerate(a_vals):
    ax.text(i - width / 2, v + 1, str(v), ha="center")
for i, v in enumerate(b_vals):
    ax.text(i + width / 2, v + 1, str(v), ha="center")

ax.set_xticks(list(x))
ax.set_xticklabels(labels)
ax.set_ylabel("debt")
ax.set_title(f"the total never moves: {books_total_before} before, {books_total_after} after")
ax.legend()
fig.tight_layout()
fig.savefig("part2-metaphor/figures/c_ledger.png", dpi=110)
print("saved part2-metaphor/figures/c_ledger.png")

# %% [markdown]
# ## What just happened, and what did not
#
# What happened: the cost was conserved. Every unit of it is still on the books.
# It is all sitting with Model B now. Model A walks away clean, and the record of
# its failures is still legible above. That is the shape of substitution.
#
# What did not happen: nothing got cheaper. If you want the "grace" here to feel
# free, notice it is only free for A. B is holding 40-something units of cost it
# did not create.
#
# Where this stops being a real analogy: a Python list does not suffer. Move to
# `where-the-analogy-breaks.md`.
