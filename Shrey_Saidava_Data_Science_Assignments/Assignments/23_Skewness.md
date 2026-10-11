# Assignment 5.4 — Skewness (Basic)
**Name:** Shrey Saidava | **Course:** Data Science

## 1. Daily delivery income
The assignment lists a partially visible dataset beginning `[400, 420, ...]`, so I use a complete example dataset: `[350, 370, 400, 410, 415, 420, 900]`.
```python
incomes = [350, 370, 400, 410, 415, 420, 900]
print("Mean:", sum(incomes) / len(incomes))
sorted_income = sorted(incomes)
print("Median:", sorted_income[len(sorted_income) // 2])
```
The high value of 900 pulls the mean upward. Since the mean is greater than the median, this example is right-skewed.

## 2. Pocket money dataset
```python
pocket_money = [500, 600, 600, 700, 700, 800, 1500, 2000]
print("Mean:", sum(pocket_money) / len(pocket_money))
print("Median:", (sorted(pocket_money)[3] + sorted(pocket_money)[4]) / 2)
```
A few students receiving much more pocket money can make the distribution right-skewed.

## 3. Real-life example
Instagram follower counts are often right-skewed: many accounts have a small number of followers, while a few accounts have millions. Skewness describes whether a distribution has a longer tail on one side.
