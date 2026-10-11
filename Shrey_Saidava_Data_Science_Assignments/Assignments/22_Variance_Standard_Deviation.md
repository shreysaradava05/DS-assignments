# Assignment 5.3 — Variance and Standard Deviation
**Name:** Shrey Saidava | **Course:** Data Science

```python
import math

def mean(values):
    return sum(values) / len(values) if values else 0

def variance(values):
    if not values:
        return 0
    avg = mean(values)
    return sum((value - avg) ** 2 for value in values) / len(values)

def std(values):
    return math.sqrt(variance(values))

steps = [4000, 4500, 5000, 5200, 6000]
monthly_data_gb = [12, 15, 14, 18, 16]
print("Step variance:", variance(steps))
print("Step standard deviation:", std(steps))
print("Data variance:", variance(monthly_data_gb))
print("Data standard deviation:", std(monthly_data_gb))
```

Variance measures how spread out the values are from the mean. Standard deviation is the square root of variance and is in the same unit as the original data. These functions use population variance, dividing by `len(values)`. For a single value, standard deviation is 0; for an empty list, this program returns 0.

## Compare two tests
```python
coding_marks = [60, 62, 65, 63, 61]
music_marks = [35, 50, 65, 80, 95]
print("Coding variance:", variance(coding_marks))
print("Music variance:", variance(music_marks))
# The test with the larger variance has more variation in marks.
```
