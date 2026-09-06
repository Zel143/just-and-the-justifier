# CLAUDE.md

Context for a Claude Code session working in this repo.

## What this repo is

An exploration of one claim (the thesis, verbatim from the README):

> At the cross, the offended pays the offender's debt so the offender goes free.

Machine learning is the vehicle, not the subject. Small auditable models make the
idea legible. Part 3 looks at the one place society already runs a
justice-versus-mercy algorithm for real: risk assessment in the courts.

## The governing test (applies to everything)

Every illustration must **conserve the cost, not reduce it.** Substitution keeps
the full penalty and changes who pays. Anything that only shrinks the penalty is
cheap grace and is cut. Where the analogy cannot conserve the cost, the repo says
so: `part2-metaphor/where-the-analogy-breaks.md`.

## Voice

The prose is Ranzel's, plain and compressed, first person, **no dashes** anywhere
(use commas, colons, or split the sentence). Scripture is quoted in ESV, exactly
as printed. Deity pronouns are capitalized (He, His) except inside quotations.
When editing prose, match that.

## Hard ethical line

This repo does **not** build a risk-scoring model and does not tune one toward
leniency. Part 3 reproduces an already-published analysis (ProPublica 2016) to
re-derive a known result (Chouldechova 2017) and reads it theologically. No model
is trained. Do not propose a "grace-adjusted" scorer.

## Layout

| Path | What |
| --- | --- |
| `part1-anchor/01-*.md`, `02-*.md` | anchor essays: the ledger, the test |
| `part2-metaphor/a_the_loss_is_real.py` | loss does not reach zero |
| `part2-metaphor/b_cost_sensitive_learning.py` | who pays for each error is a moral choice |
| `part2-metaphor/c_the_two_model_ledger.py` | centerpiece: cost fully paid and transferred (stdlib only) |
| `part2-metaphor/d_calibration.py` | a merciful verdict can still be true; sets up Part 3 |
| `part2-metaphor/where-the-analogy-breaks.md` | the honesty file |
| `part3-case-study/reproduce_the_impossibility.py` | COMPAS reproduction, no training |
| `part3-case-study/reading.md` | theological reading of the result |
| `part4-synthesis/the-thing-no-optimization-reaches.md` | closing essay |

## Environment

- Runs in the **Ubuntu** WSL distro. `/mnt/g` is mounted. Virtualenv at `.venv/`.
- Python 3.14, with numpy 2.5.2 / pandas 3.0.5 / scikit-learn 1.9.0 / matplotlib.
- `python part2-metaphor/c_the_two_model_ledger.py` needs only the standard library.
- COMPAS CSV is not committed. `data/README.md` has the one-line curl command.

## Verifying the code

```bash
source .venv/bin/activate
python part2-metaphor/a_the_loss_is_real.py     # loss settles at the noise floor, not zero
python part2-metaphor/b_cost_sensitive_learning.py  # higher fp cost raises the threshold
python part2-metaphor/c_the_two_model_ledger.py     # A ledger = 0, total unchanged
python part2-metaphor/d_calibration.py              # unequal error rates across groups
python part3-case-study/reproduce_the_impossibility.py   # reproduces ProPublica's numbers
```
