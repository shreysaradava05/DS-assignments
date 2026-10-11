# Assignment 2.8 — Loops
**Name:** Shrey Saidava | **Course:** Data Science

## 1. Total of ten order prices
```python
order_prices = [250, 400, 150, 600, 300, 220, 180, 750, 340, 500]
total = 0
for price in order_prices:
    total += price
print("Total order amount:", total)
```

## 2. Delivery countdown
```python
minutes = 10
while minutes >= 0:
    print(minutes)
    minutes -= 1
print("Delivery countdown finished")
```

## 3. Stop when likes exceed 1000
```python
post_likes = [120, 450, 980, 1250, 700, 1600]
for likes in post_likes:
    print(likes)
    if likes > 1000:
        print("Found a post with more than 1000 likes")
        break
```

## 4. Number each playlist
```python
playlists = ["Workout", "Chill", "Study", "Pop", "Rock", "Travel", "Focus", "Favorites"]
for number, name in enumerate(playlists, start=1):
    print(number, name)
```
A `for` loop goes through items in a sequence. A `while` loop repeats while its condition is true. `break` stops a loop early.
