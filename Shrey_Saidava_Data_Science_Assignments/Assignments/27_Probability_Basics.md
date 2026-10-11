# Assignment 5.8 — Probability Basics
**Name:** Shrey Saidava | **Course:** Data Science

## 1. Simple probability function
```python
def calculate_probability(favorable_outcomes, total_outcomes):
    if total_outcomes <= 0:
        return 0
    return favorable_outcomes / total_outcomes

print(calculate_probability(3, 10))
```

## 2. Simulate a fair coin 20 times
```python
import random

results = [random.choice(["Heads", "Tails"]) for _ in range(20)]
heads = results.count("Heads")
print(results)
print("Heads count:", heads)
print("Experimental probability:", heads / 20)
```
The experimental probability may not be exactly 0.5 in only 20 tosses.

## 3. Probability of an even number on a die
```python
def even_probability():
    even_numbers = [2, 4, 6]
    return len(even_numbers) / 6

print(even_probability())
```

## 4. Cards
A standard deck has 52 cards and 4 aces, so P(Ace) = 4/52 = 1/13. There are 26 red cards, so the probability of drawing one red card from a well-shuffled deck is 26/52 = 1/2. If “3 red cards” means drawing three cards without replacement and all three must be red, the probability is `(26/52) * (25/51) * (24/50)`.

## 5. Pizza order is at night
Night orders = 60% of all orders; 30% of night orders are pizza. Day orders = 40%; 10% of day orders are pizza.
- P(night and pizza) = 0.60 × 0.30 = 0.18
- P(day and pizza) = 0.40 × 0.10 = 0.04
- P(pizza) = 0.18 + 0.04 = 0.22
- P(night | pizza) = 0.18 / 0.22 ≈ 0.8182, or **81.82%**.
