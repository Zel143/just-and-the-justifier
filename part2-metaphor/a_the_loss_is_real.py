# %% [markdown]
# # Notebook A: the loss is real
#
# The demand of justice, in the plainest ML terms: error has to be accounted for.
# A loss function does not go to zero because you want it to. When there is real
# irreducible noise in the world, the loss bottoms out above zero and stays
# there, no matter how long you train.
#
# The point of this notebook is small and it is not a trick: you cannot optimize
# your way out of a debt that is actually owed.

# %% [markdown]
# ## Reflection
#
# The loss does not go to zero because the noise is really there. You can train
# forever and it will not help. That is closer to sin than I expected a straight
# line fit to get. Sin is not a bookkeeping mistake that a cleaner ledger clears.
# Something is actually owed. The honest model is the one that reports the
# residual it cannot remove instead of claiming it accounted for everything. A
# model that shows zero loss is lying. It has memorized the noise and called it
# signal. I think we do the same thing when we tell ourselves the wrong was
# smaller than it was. The first honest move is to stop discounting the number.

# %%
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(26)

# %% [markdown]
# ## A world with irreducible noise
#
# The true relationship is y = 2x + 1. But every observation carries noise we
# cannot predict or remove. That noise is the irreducible loss: the part of the
# error that is really there.

# %%
NOISE_SD = 1.5

def make_data(n):
    x = rng.uniform(-3, 3, n)
    y = 2 * x + 1 + rng.normal(0, NOISE_SD, n)
    return x, y

# Train on one sample, judge on data we have not seen. The honest question is not
# "how low can the loss go on the data we fit" but "how low can it go on new
# data." That second number cannot beat the noise floor, in expectation.
x, y = make_data(400)

irreducible_mse = NOISE_SD ** 2  # the best any model can do, in expectation
print(f"Irreducible MSE (the floor): {irreducible_mse:.3f}")

# %% [markdown]
# ## Train a model that has every advantage
#
# Correct functional form, clean optimizer, as many steps as we want.

# %%
w, b = 0.0, 0.0
lr = 0.05
history = []
for step in range(2000):
    y_hat = w * x + b
    err = y_hat - y
    mse = np.mean(err ** 2)
    history.append(mse)
    grad_w = 2 * np.mean(err * x)
    grad_b = 2 * np.mean(err)
    w -= lr * grad_w
    b -= lr * grad_b

# Measure the trained model on many fresh samples and average. A single test set
# wobbles by chance. The average estimates the loss this model really carries.
test_mses = [np.mean((w * xt + b - yt) ** 2)
             for xt, yt in (make_data(2000) for _ in range(200))]
test_mse = float(np.mean(test_mses))

print(f"Recovered w = {w:.3f} (true 2.0), b = {b:.3f} (true 1.0)")
print(f"Final training MSE:   {history[-1]:.3f}")
print(f"Mean loss on new data: {test_mse:.3f}")
print(f"Noise floor:          {irreducible_mse:.3f}")
print(f"Zero, for comparison:  0.000")

# %%
assert abs(w - 2.0) < 0.15 and abs(b - 1.0) < 0.15, "model did not converge"
assert abs(test_mse - irreducible_mse) < 0.1, (
    "loss did not settle at the noise floor"
)
assert test_mse > 1.0, "loss got near zero, which the noise makes impossible"
print("PASS: the model recovered the true line, the loss settled at the noise "
      "floor, and the floor is not zero.")

# %% [markdown]
# ## The picture

# %%
fig, ax = plt.subplots(1, 2, figsize=(11, 4))
ax[0].scatter(x, y, s=12, alpha=0.5)
xs = np.linspace(-3, 3, 50)
ax[0].plot(xs, w * xs + b, color="black", label="fitted")
ax[0].plot(xs, 2 * xs + 1, color="crimson", ls="--", label="true")
ax[0].set_title("the fit is right; the scatter is real")
ax[0].legend()

ax[1].plot(history, color="black")
ax[1].axhline(irreducible_mse, color="crimson", ls="--", label="noise floor")
ax[1].set_xlabel("step")
ax[1].set_ylabel("MSE")
ax[1].set_title("loss falls, then stops above zero")
ax[1].legend()

fig.tight_layout()
fig.savefig("part2-metaphor/figures/a_loss_floor.png", dpi=110)
print("saved part2-metaphor/figures/a_loss_floor.png")

# %% [markdown]
# ## Where this points
#
# A model that drove this loss to zero would not be more righteous. It would be
# lying: fitting the noise, claiming to account for what cannot be accounted for
# by prediction. The honest model carries a residual it cannot remove.
#
# Notebook C is about what happens when someone else carries it.
