# Assignment 2.11 — Recursion and Scope
**Name:** Shrey Saidava | **Course:** Data Science

## 1. Recursive total play counts
```python
def total_plays(plays):
    if len(plays) == 0:
        return 0
    return plays[0] + total_plays(plays[1:])

print(total_plays([120, 80, 150, 200]))
```

## 2. Reverse a string without a built-in reverse function
```python
def reverse_text(text):
    if len(text) <= 1:
        return text
    return reverse_text(text[1:]) + text[0]

print(reverse_text("spotify"))
```

## 3. Scope example
```python
discount = 5

def apply_coupon(price):
    discount = 10  # local variable; does not change the global variable
    return price * (1 - discount / 100)

print(apply_coupon(1000))
print("Global discount:", discount)
```
Recursion is when a function calls itself. It needs a base case to stop. A local variable belongs to a function, while a global variable is defined outside it.
