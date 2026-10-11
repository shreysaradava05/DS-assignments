import math
def mean(values): return sum(values) / len(values) if values else 0
def variance(values):
    if not values: return 0
    avg = mean(values)
    return sum((value - avg) ** 2 for value in values) / len(values)
def std(values): return math.sqrt(variance(values))
values = [4000, 4500, 5000, 5200, 6000]
print("Variance:", variance(values))
print("Standard deviation:", std(values))
