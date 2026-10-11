# Assignment 5.9 — Normal Distribution
**Name:** Shrey Saidava | **Course:** Data Science

## 1. Generate 1,000 values and plot a bell curve
```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(10)
data = np.random.normal(loc=50, scale=10, size=1000)
mean_value = np.mean(data)
std_value = np.std(data)

plt.hist(data, bins=30, density=True, alpha=0.6, edgecolor="black")
x = np.linspace(min(data), max(data), 300)
y = (1 / (std_value * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean_value) / std_value) ** 2)
plt.plot(x, y)
plt.axvline(mean_value, linestyle="--", label="Mean")
plt.fill_between(x, y, where=(x >= mean_value - std_value) & (x <= mean_value + std_value), alpha=0.25, label="Within 1 SD")
plt.fill_between(x, y, where=(x >= mean_value - 2*std_value) & (x <= mean_value + 2*std_value), alpha=0.15, label="Within 2 SD")
plt.fill_between(x, y, where=(x >= mean_value - 3*std_value) & (x <= mean_value + 3*std_value), alpha=0.08, label="Within 3 SD")
plt.xlabel("Value")
plt.ylabel("Density")
plt.title("Normal Distribution")
plt.legend()
plt.show()
```

## 2. Count data within standard-deviation ranges
```python
for number in [1, 2, 3]:
    low = mean_value - number * std_value
    high = mean_value + number * std_value
    count = np.sum((data >= low) & (data <= high))
    print(f"Within {number} standard deviation(s): {count} values ({count / len(data) * 100:.1f}%)")
```
For a normal distribution, about 68% of values fall within 1 standard deviation, 95% within 2, and 99.7% within 3. The generated sample may be slightly different.
