# Assignment 5.10 — Bayes Theorem (Basic)
**Name:** Shrey Saidava | **Course:** Data Science

## 1. Formula
Bayes’ theorem is:

**P(A | B) = P(B | A) × P(A) / P(B)**

It updates the probability of an event after new evidence is observed. `P(A)` is the prior probability, `P(B | A)` is the likelihood, and `P(A | B)` is the posterior probability.

## 2. Spam email example
The visible assignment gives 1,000 emails and says 200 are spam, but the remaining keyword-match figures are unclear in the scan. Therefore, a unique numeric answer cannot be calculated from the provided information. If, for example, 160 of the 200 spam emails contain a keyword and 80 of the 800 non-spam emails also contain it, then:
- Prior spam probability = 200/1000 = 0.20
- Likelihood of keyword given spam = 160/200 = 0.80
- Evidence probability = (160 + 80)/1000 = 0.24
- Posterior = 0.80 × 0.20 / 0.24 = 0.6667, or 66.67%
These extra counts are only an example, not values readable from the assignment.

## 3. Rapid-test example
If prevalence is 9%, sensitivity is 98%, and specificity is 95%, then false-positive rate is 5%.
- P(COVID and positive) = 0.09 × 0.98 = 0.0882
- P(no COVID and positive) = 0.91 × 0.05 = 0.0455
- P(positive) = 0.0882 + 0.0455 = 0.1337
- P(COVID | positive) = 0.0882 / 0.1337 ≈ **65.97%**

## 4. App example
Gmail could use Bayes’ theorem to estimate whether a new email is spam. The prior is the general chance an email is spam, and the evidence includes words, sender information, and links. After seeing the evidence, the system calculates a posterior probability and can move high-risk messages to spam.
