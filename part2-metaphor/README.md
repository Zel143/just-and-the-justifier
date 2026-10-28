# part2-metaphor

Four small notebooks. ML as the metaphor vehicle, held to the conserve-versus-
reduce test from Part 1.

| File | Level | Needs libs | One line |
| --- | --- | --- | --- |
| `a_the_loss_is_real.py` | 2, linear regression by hand | numpy, matplotlib | the loss does not reach zero because you want it to |
| `b_cost_sensitive_learning.py` | 2, logistic regression | numpy, scikit-learn | who gets charged for each kind of mistake is a moral choice |
| `c_the_two_model_ledger.py` | 1, deterministic rules | stdlib (matplotlib optional, for the figure) | the centerpiece: cost fully paid, fully transferred |
| `d_calibration.py` | 2, logistic regression | numpy, scikit-learn, matplotlib | a merciful verdict can still be a true one; sets up Part 3 |

**Level** is the rung of the smallest-model-first hierarchy each notebook stops at:

0. No model: descriptive statistics only
1. Deterministic rules and arithmetic
2. Classical statistical ML: linear or logistic regression, trees, naive Bayes
3. Gradient boosting on tabular data
4. Small task-specific deep models
5. Generative LLMs

No notebook here goes above level 2. Part 3 stays at level 0 by rule: it trains
nothing. Why each notebook stops where it does is an open question in
`../QUESTIONS.md` (Q9 to Q12).

Each `.py` is a `# %%` cell script. Run with `python <file>` from the repo root,
or open as a notebook in VS Code. Figures land in `figures/`.

Every notebook has a **Reflection** cell near the top.

Also here: `where-the-analogy-breaks.md`, the honesty file. Not optional.
