# Assignment 5.2 — Mean, Median and Mode
**Name:** Shrey Saidava | **Course:** Data Science

```python
from collections import Counter

def mean(arr):
    if not arr:
        return 0
    return sum(arr) / len(arr)

def median(arr):
    if not arr:
        return None
    values = sorted(arr)
    middle = len(values) // 2
    if len(values) % 2 == 1:
        return values[middle]
    return (values[middle - 1] + values[middle]) / 2

def mode(arr):
    if not arr:
        return None
    counts = Counter(arr)
    highest = max(counts.values())
    return [value for value, count in counts.items() if count == highest]

steps = [250, 400, 150, 600, 300]
print("Mean steps:", mean(steps))
print("Median steps:", median(steps))
print("Mode steps:", mode(steps))

listening_seconds = [180, 240, 180, 300, 240, 180]
print("Listening mean:", mean(listening_seconds))
print("Listening median:", median(listening_seconds))
print("Listening mode:", mode(listening_seconds))
```

Mean is the total divided by the number of values. Median is the middle value after sorting. Mode is the most frequent value. For data with extreme values, the median often describes a typical value better than the mean.
