# Questions

A working log. Each question gets answered here in my own words before any prose
or code in the repo changes because of it.

## Method

1. **Predict before you run.** Write down what a notebook will print before
   running it. The gap between the guess and the output is the lesson.
2. **Write before you ask.** Draft the answer here first. An assistant may check
   it, question it, or point at a contradiction. It does not write it.
3. **One question at a time.** A question is closed when the Decision line is
   filled in and the repo matches it.
4. **Smallest model first.** Before reaching for any tool, name the lowest level
   that answers the question, and say why the next level up adds nothing. The
   levels: 0 descriptive statistics, 1 deterministic rules, 2 classical
   statistical ML, 3 gradient boosting, 4 small task-specific deep models,
   5 generative LLMs. See `part2-metaphor/README.md` for where each notebook sits.

Entry format: the question, why it matters, my answer, the decision.

---

## Q1: Is the cross a balance between justice and grace, or both in full?

**Why it matters.** "Balance" suggests a dial with a best setting in the middle.
Part 4 says the cross is not that.

**Your answer:** Both in full, in one act. Not a balance.

**Decision:** The repo does not describe the cross as a tradeoff. See Q6 for the
places where the word "balance" still appears.

## Q2: What are justice and grace as properties of a ledger?

**Why it matters.** Right now the definitions are spread across essays 01 and 02
and Notebook C. A data scientist should be able to read one sentence for each and
know what to check.

**Your answer:**

**Decision:**

## Q3: What are the four cells?

**Why it matters.** Two yes or no questions give four outcomes. Is the total cost
still on the books? Does the offender still carry it? Name all four cells in your
own terms. Is the fourth one real, or does it fold into another?

**Your answer:**

**Decision:**

## Q4: Which sentence is the thesis?

**Why it matters.** The README opens with one sentence about the crucifixion and
then gives a different one under "Thesis". Do they say the same thing? If not,
which one does the repo defend?

**Your answer:**

**Decision:**

## Q5: Does Notebook B conserve the cost, or redistribute it?

**Why it matters.** The last cell of `b_cost_sensitive_learning.py` says
cost-sensitive learning "conserves cost in the accounting sense." The notebook
moves errors between false positives and false negatives. Run that against your
own test from essay 02 and rewrite the claim.

**Your answer:**

**Decision:**

## Q6: Does "balanced ledger" survive Q1?

**Why it matters.** The title of essay 01 and the README structure table use
"balanced ledger". Does "balanced" mean "the books balance", which fits, or "a
balance between two goods", which Q1 rules out? Will a reader know which one?

**Your answer:**

**Decision:**

## Q7: When was Kleinberg et al.?

**Why it matters.** The code comments now say 2016 preprint, ITCS 2017.
`reading.md` says "the same year as Chouldechova", which is 2017. Which year do
you mean, and what should that sentence say?

**Your answer:**

**Decision:**

## Q8: Practice, predict Notebook C

**Why it matters.** This is the method in miniature. Before running
`part2-metaphor/c_the_two_model_ledger.py`, read the code only.

**Your prediction:** how many mistakes does Model A make, and what is Model B's
final debt? Roughly is fine, but give a reason.

**Actual output:**

**What the gap taught me:**

---

# The model choice audit

Q9 to Q12 are asked of each Part 2 notebook. Part 3 is left out on purpose: it
stays at level 0 and trains nothing, so there is no model choice to audit there.

## Q9: Framing. What is each notebook actually testing?

**Why it matters.** A precise model starts with a precise target. For each
notebook: what is the claim, what goes in, what comes out, and does the assert
at the end test the claim itself or something next to it?

| Notebook | Claim | Input | Target | Does the assert test the claim? |
| --- | --- | --- | --- | --- |
| A | | | | |
| B | | | | |
| C | | | | |
| D | | | | |

**Decision:**

## Q10: Cost. What would a reader have to trust?

**Why it matters.** Every notebook runs in seconds, so compute is not the cost
that matters. The cost that matters is a reader checking the claim. If a step
were an LLM call instead of the code it is now, what would the reader have to
take on trust?

| Notebook | What the reader can verify now | What they would have to trust instead |
| --- | --- | --- |
| A | | |
| B | | |
| C | | |
| D | | |

**Decision:**

## Q11: Interpretability. Can it be checked by hand?

**Why it matters.** The repo's argument rests on readers seeing the number move,
not taking it on faith. Can a reader check each result with a pencil? Which
notebook is the hardest to check, and why?

| Notebook | Checkable by hand? | What makes it hard, if anything |
| --- | --- | --- |
| A | | |
| B | | |
| C | | |
| D | | |

**Hardest one and why:**

**Decision:**

## Q12: Failure and determinism. Does the claim survive another seed?

**Why it matters.** Every notebook seeds its random numbers with 26. A claim that
holds only for one seed is a coincidence, not a claim. Predict first, then change
the seed and run.

| Notebook | Prediction: passes on other seeds? | Why | Actual |
| --- | --- | --- | --- |
| A | | | |
| B | | | |
| C | | | |
| D | | | |

**What the gap taught me:**

**Decision:**
