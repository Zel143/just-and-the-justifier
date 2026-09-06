# data/

This repo does not ship any dataset. Part 3 uses one public, already-published
file.

## compas-scores-two-years.csv

ProPublica's dataset from their 2016 investigation "Machine Bias". It is the
exact file behind a published analysis, used here only to re-derive a known
mathematical result.

Download it:

```bash
curl -L -o data/compas-scores-two-years.csv \
  https://raw.githubusercontent.com/propublica/compas-analysis/master/compas-scores-two-years.csv
```

Source repo: https://github.com/propublica/compas-analysis
Article: https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing

## What is not done with it

No model is trained. No score is produced. No threshold is tuned to be lenient.
The notebook computes summary statistics that ProPublica and later Chouldechova
(2017) and Kleinberg et al. (2016) already published, and reads them
theologically. See `../README.md`, section "What this repo is not".
