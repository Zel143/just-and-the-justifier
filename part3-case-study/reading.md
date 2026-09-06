# Reading the impossibility result

The notebook beside this file does not build anything. It loads a public dataset,
reproduces a result that was already published, and stops. Three facts come out
of it, and this essay reads them.

First, the two groups in the data reoffend at different rates. That gap is in the
world the data came from, not in the algorithm. Second, COMPAS is roughly
calibrated across the two groups. A given score means about the same chance of
reoffending whichever group you are in. Third, once both of those hold, the
groups cannot also have equal false positive and false negative rates.
Chouldechova proved this in 2017. It is arithmetic, not a bug someone forgot to
fix.

That is the shape of the argument that actually happened. ProPublica said COMPAS
was biased because the error rates came out different by race. Northpointe
answered that the score was calibrated, so it was fair. Both were reading the
data correctly. The fight was never about the numbers. It was about which
definition of fair to use, and the math says you cannot hold both at once.

Here is what those facts look like next to Part 1.

**A false positive is a wrongful condemnation.** It is a person the system
flagged as a future danger who turned out not to be. The machine treated them as
guilty of something they had not done and were not going to do. Scripture does
not treat that lightly. "He who justifies the wicked and he who condemns the
righteous are both alike an abomination to the LORD." The system manages both
errors at once, and it does not spread them evenly across groups.

**The base rate gap is inherited harm.** The people being scored did not choose
the conditions that produced the gap. Generations of policing, housing, and
prosecution shaped those numbers before anyone in the dataset was born. And the
outcome the model predicts, rearrest within two years, is partly a measure of who
gets watched, not only who reoffends. A model asked to predict something history
has bent will carry the bend forward and print it as a risk score. This is not a
claim that individual acts do not matter. The harm is real, and it is not the
fault of the person now standing in front of the judge.

There is an old word for harm that arrives ahead of the person who carries it.
Scripture keeps returning to it: consequences running down generations, a world
every one of us is born into rather than chooses. That is the deep pattern. The
data shows one modern, measurable instance of it.

**Moving the threshold is not grace.** You can lower the cutoff and flag fewer
people. It feels like mercy. But the harm the score was pointing at did not go
anywhere. It lands somewhere, on a future victim, on the next case, on the person
who was flagged and then was not. The system just stopped naming it. This is the
conserve-versus-reduce test from essay 02, moved from a notebook to a policy.
Lowering a threshold reduces. It does not conserve. Cheap grace has an
algorithmic form, and this is what it looks like.

**A sorting machine cannot redeem.** COMPAS puts people in bins. That is the
whole of what it does. It has no way to restore anyone, no account of what a
person is for, no step that makes a wronged party whole. Retributive prediction
and reconciliation are different activities, and no amount of tuning turns one
into the other. Part 1 said the cross is not a better sorting, it is a
substitution followed by a restoration. A risk score has neither half.

## Why this repo does not build a kinder version

The obvious next move is to build a "grace-adjusted" score, tuned to be lenient,
and call it the Christian one. This repo does not, for two reasons.

Technically, there is nothing to build. Kleinberg and his coauthors showed, the
same year as Chouldechova, that you cannot have calibration and equal error rates
together when base rates differ. Every "fairer" score is a choice about which one
to break. Calling that choice mercy does not make it mercy. It makes it a
preference with a nicer name.

Morally it is worse. A lower score does not carry anyone's cost. The debt essay
01 is about, someone actually pays it. A leniency knob pays nothing. It moves
risk onto people who are not in the dataset and cannot see it happening, and it
lets the person turning the knob feel merciful for doing so. That is the thesis
turned inside out. The offended pays so the offender goes free. A tuned threshold
makes an unnamed third party pay so the tuner feels better.

What the machine can honestly do here is show you the trap. It cannot get you out
of it. Getting out was never an optimization problem.
