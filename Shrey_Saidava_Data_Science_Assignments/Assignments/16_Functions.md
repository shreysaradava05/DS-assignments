# Assignment 2.9 — Functions
**Name:** Shrey Saidava | **Course:** Data Science

## 1. Final price after discount
```python
def get_final_price(price, discount):
    return price - (price * discount / 100)

print(get_final_price(1000, 10))  # 900.0
```

## 2. Format username
```python
def format_username(name):
    return name.strip().lower().replace(" ", "")

print(format_username(" Shrey Saidava "))  # shreysaidava
```

## 3. Split a bill
```python
def split_bill(total_amount, num_people=2):
    if num_people <= 0:
        raise ValueError("Number of people must be greater than zero")
    return total_amount / num_people

print(split_bill(900))
print(split_bill(900, 3))
```

## 4. Delivery charge
```python
def get_delivery_charge(order_amount, city="Ahmedabad"):
    if order_amount >= 500:
        return 0
    if city.lower() == "ahmedabad":
        return 40
    return 60

print(get_delivery_charge(300))
print(get_delivery_charge(300, "Surat"))
```

## 5. Apply coupon
```python
def apply_coupon(price, coupon=None):
    if coupon == "SAVE10":
        return price * 0.90
    return price

print(apply_coupon(1000, "SAVE10"))
print(apply_coupon(1000))
```
Functions let me reuse code and make a program easier to read.
