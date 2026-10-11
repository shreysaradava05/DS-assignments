# Assignment 2.7 — Conditional Statements
**Name:** Shrey Saidava | **Course:** Data Science

## 1. Music break reminder
```python
minutes_listened = int(input("Minutes listened today: "))
if minutes_listened >= 120:
    print("Take a break!")
else:
    print("Keep enjoying your music!")
```

## 2. Free delivery
```python
order_amount = float(input("Enter order amount: ₹"))
if order_amount >= 500:
    print("Eligible for free delivery")
else:
    print("Delivery charges apply")
```

## 3. Player level
```python
points = int(input("Enter your points: "))
if points < 100:
    print("Beginner")
elif points < 500:
    print("Pro Player")
else:
    print("Expert Player")
```

## 4. Nested if example
```python
age = int(input("Enter age: "))
has_id = input("Do you have a valid ID? (yes/no): ").lower()
if age >= 18:
    if has_id == "yes":
        print("Entry allowed")
    else:
        print("Please show a valid ID")
else:
    print("Entry not allowed")
```
A conditional statement runs different code depending on whether a condition is true or false.
