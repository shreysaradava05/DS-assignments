# Assignment 2.10 — Lambda, Map, Filter and Reduce
**Name:** Shrey Saidava | **Course:** Data Science

## 1. Clean product names
```python
products = ["  pizza", "BURGER  ", "  Ice Cream "]
clean_products = list(map(lambda name: name.strip().title(), products))
print(clean_products)
```

## 2. Lambda for total bill
```python
prices = [100, 250, 75]
total_bill = (lambda values: sum(values))(prices)
print("Total bill:", total_bill)
```

## 3. Filter ratings of 4 and above
```python
ratings = [3.2, 4.5, 5.0, 2.8, 4.0, 3.9]
high_ratings = list(filter(lambda rating: rating >= 4, ratings))
print(high_ratings)
```

## 4. Filter and calculate total order value
```python
from functools import reduce
orders = [120, 650, 240, 800, 90]
large_orders = list(filter(lambda amount: amount >= 500, orders))
total_large_orders = reduce(lambda total, amount: total + amount, large_orders, 0)
print("Large orders:", large_orders)
print("Total:", total_large_orders)
```
`lambda` makes a small anonymous function, `map` transforms items, `filter` selects items, and `reduce` combines items into one result.
