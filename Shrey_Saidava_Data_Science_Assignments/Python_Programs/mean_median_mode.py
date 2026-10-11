from collections import Counter
def mean(arr):
    return sum(arr) / len(arr) if arr else 0
def median(arr):
    if not arr: return None
    values = sorted(arr); middle = len(values) // 2
    return values[middle] if len(values) % 2 else (values[middle - 1] + values[middle]) / 2
def mode(arr):
    if not arr: return None
    counts = Counter(arr); highest = max(counts.values())
    return [value for value, count in counts.items() if count == highest]
values = [250, 400, 150, 600, 300]
print(mean(values), median(values), mode(values))
