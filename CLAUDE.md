# CLAUDE.md

Context for any Claude Code session working in this repo. Read this first.

## What this repo is

An exploration of one claim (the thesis, verbatim from the README):

> At the cross, the offended pays the offender's debt so the offender goes free.

Justice was satisfied rather than waived. Grace is the offended party choosing to
pay rather than collect.

Machine learning is the **vehicle**, not the subject. Small, auditable models
make the idea legible. Then Part 3 looks at the one place society already runs a
justice-versus-mercy algorithm for real: risk assessment in the courts.

Audience: a LinkedIn portfolio piece, and personal study. Author: Ranzel.

## The governing test (applies to everything)

Every illustration must **conserve the cost, not reduce it.**

- Conserve: the full penalty is still paid, only the payer changes. This is
  substitution. This is the cross.
- Reduce: the penalty is made smaller, softened, or dropped. This is cheap grace
  and it is cut from the repo.

Where the analogy cannot conserve the cost, the repo says so plainly. See
`part2-metaphor/where-the-analogy-breaks.md`.

## Division of labor (important, do not cross this line)

**All prose is Ranzel's to draft. Claude reviews only, never ghostwrites it.**

- Essays and the notebook `Reflection` cells: he writes them, in his own voice,
  RAW register first then STRUCTURED. See `WRITING.md`.
- No dashes anywhere in the prose. Commas, colons, parentheses, or split the
  sentence.
- Claude wrote and maintains all the code and scaffolding.
- When asked to "help with" an essay: coach and review. Ask what is not landing,
  point at hand-waving, check claims against the governing test. Do not hand back
  rewritten paragraphs.

Draft spots are marked `TODO` in every file. `grep -rn TODO .` lists them.

## Hard ethical line

This repo does **not** build a risk-scoring model and does not tune one toward
leniency. Part 3 reproduces an already-published analysis (ProPublica's 2016
COMPAS study) to re-derive a known mathematical result (Chouldechova 2017), and
reads it theologically. No model is trained. A "grace-adjusted" recidivism scorer
would be the exact cheap grace the repo argues against, and it would cause real
harm. Do not propose one.

## Layout

| Path | What | Status |
| --- | --- | --- |
| `part1-anchor/01-*.md`, `02-*.md` | anchor essays: the ledger, the test | outline only, Ranzel to write |
| `part2-metaphor/a_the_loss_is_real.py` | loss does not reach zero | code done, reflection TODO |
| `part2-metaphor/b_cost_sensitive_learning.py` | who pays for each error is a moral choice | code done, reflection TODO |
| `part2-metaphor/c_the_two_model_ledger.py` | centerpiece: cost fully paid and transferred | code done and PASSES, reflection TODO |
| `part2-metaphor/d_calibration.py` | a merciful verdict can still be true; sets up Part 3 | code done, reflection TODO |
| `part2-metaphor/where-the-analogy-breaks.md` | the honesty file | starter points, Ranzel to finish |
| `part3-case-study/reproduce_the_impossibility.py` | COMPAS reproduction, no training | code done, needs the CSV |
| `part3-case-study/reading.md` | theological reading of the result | outline only, Ranzel to write |
| `part4-synthesis/the-thing-no-optimization-reaches.md` | closing essay | outline only, Ranzel to write |

## Environment

- Runs in the **Ubuntu** WSL distro (not `docker-desktop`). `/mnt/g` is mounted
  here. VS Code must be connected to the Ubuntu distro.
- Python 3.14. Virtualenv at `.venv/`.
- `python part2-metaphor/c_the_two_model_ledger.py` works with system Python
  (standard library only).
- Notebooks A, B, D and Part 3 need `numpy pandas scikit-learn matplotlib`.
  Verified installed and working in `.venv` (numpy 2.5.2, pandas 3.0.5,
  scikit-learn 1.9.0). If reinstalling, network here drops large downloads, use
  `pip install --resume-retries 12 -r requirements.txt`.
- COMPAS CSV is not shipped. `data/README.md` has the one-line curl command.
  Currently present at `data/compas-scores-two-years.csv` (7214 rows).
- All five notebooks / scripts run clean and pass their assertions as of
  2026-09-06.

## Verifying the code

```bash
source .venv/bin/activate
python part2-metaphor/c_the_two_model_ledger.py     # asserts: A ledger = 0, total unchanged
python part2-metaphor/a_the_loss_is_real.py         # asserts: converges, loss stays above noise floor
python part2-metaphor/b_cost_sensitive_learning.py  # asserts: higher fp cost raises the threshold
python part2-metaphor/d_calibration.py              # asserts: unequal error rates across groups
python part3-case-study/reproduce_the_impossibility.py   # needs data/compas-scores-two-years.csv
```

## Not yet done

- Repo is not a git repo yet (`git init` when ready).
- The LinkedIn post itself is not drafted.
