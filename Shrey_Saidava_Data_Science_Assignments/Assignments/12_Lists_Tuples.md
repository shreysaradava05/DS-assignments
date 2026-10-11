# Assignment 2.5 — Lists and Tuples
**Name:** Shrey Saidava | **Course:** Data Science

## 1. Playlist list
```python
playlist = ["Perfect", "Believer", "Kesariya"]
print(playlist)
```

## 2. Shopping cart
```python
cart = ["T-shirt", "Jeans", "Shoes"]
cart.append("Cap")
removed_item = cart.pop(1)
print("Removed:", removed_item)
print("Updated cart:", cart)
```

## 3. Tuple immutability
```python
fav_brands = ("Nike", "Adidas", "Puma")
print(fav_brands)
# fav_brands[0] = "Reebok"  # This raises TypeError because tuples cannot be changed.
```

## 4. Zomato order history
```python
orders = ["Pizza", "Burger", "Fries", "Pasta"]
removed_order = orders.pop(2)
print("Removed order:", removed_order)
print("Order history:", orders)
```

## 5. List vs tuple
I would use a list for IPL teams if the list may change. I would use a tuple for fixed season names that should stay unchanged.
