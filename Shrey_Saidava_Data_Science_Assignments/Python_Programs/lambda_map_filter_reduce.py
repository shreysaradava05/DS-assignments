from functools import reduce
products = ["  pizza", "BURGER  ", "  Ice Cream "]
print(list(map(lambda name: name.strip().title(), products)))
ratings = [3.2, 4.5, 5.0, 2.8, 4.0, 3.9]
print(list(filter(lambda rating: rating >= 4, ratings)))
orders = [120, 650, 240, 800, 90]
large_orders = list(filter(lambda amount: amount >= 500, orders))
print(reduce(lambda total, amount: total + amount, large_orders, 0))
