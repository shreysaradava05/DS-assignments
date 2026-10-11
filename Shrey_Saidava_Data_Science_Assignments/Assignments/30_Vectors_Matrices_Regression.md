# Assignment 5.11–5.12 — Vectors, Matrices and Linear Regression Intuition
**Name:** Shrey Saidava | **Course:** Data Science

## 1. Print a matrix of scores
```python
scores = [[90, 85, 88], [75, 80, 70], [60, 95, 90]]
for row in scores:
    print(row)
```

## 2. Multiply a 2×3 matrix by a 3×2 matrix
```python
A = [[1, 2, 3], [4, 5, 6]]
B = [[7, 8], [9, 10], [11, 12]]

result = [[0, 0], [0, 0]]
for i in range(2):
    for j in range(2):
        for k in range(3):
            result[i][j] += A[i][k] * B[k][j]

for row in result:
    print(row)
```
The result is `[[58, 64], [139, 154]]`.

## 3. Step counts and calories
```python
steps = [4000, 5000, 6000, 7000, 8000, 9000, 10000]
calories = [150, 190, 230, 260, 310, 340, 380]
print("Steps:", steps)
print("Calories:", calories)
```
The two lists contain paired daily observations. I could plot them or calculate correlation to check whether higher step counts tend to go with more calories burned. This relationship alone does not prove cause and effect.

## 4. Matrix multiplication and linear regression
Matrix multiplication combines rows and columns using multiplication and addition. Linear regression finds a line that estimates a numeric result from input values. For example, an app could use delivery distance to estimate delivery time. The model learns a relationship from previous data, then predicts an approximate time for a new order.
