# Assignment 2.3 — Data Types
**Name:** Shrey Saidava | **Course:** Data Science

## 1. Four variables
```python
student_name = "Shrey Saidava"  # string
student_gpa = 8.2                # float; example value
semester = 1                    # integer
has_spotify = True               # boolean

print(student_name, type(student_name))
print(student_gpa, type(student_gpa))
print(semester, type(semester))
print(has_spotify, type(has_spotify))
```

## 2. Convert prices to floats and add them
```python
prices = ["199.99", "349.50", "120.00"]
prices = [float(price) for price in prices]
total = sum(prices)
print("Total:", round(total, 2))
```

## 3. Offer eligibility function
```python
def is_offer_eligible(amount):
    return amount >= 500

print(is_offer_eligible(650))  # True
print(is_offer_eligible(300))  # False
```

## 4. Mask a phone number
```python
phone = input("Enter your phone number: ")
phone = str(phone)
print("X" * max(0, len(phone) - 4) + phone[-4:])
```
This displays only the last four digits. I should not print or share a real phone number in public examples.
