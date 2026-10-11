# Assignment 2.6 — Dictionaries and Sets
**Name:** Shrey Saidava | **Course:** Data Science

## 1. Playlist durations
```python
playlist_durations = {
    "Workout": 45,
    "Relax": 30,
    "Study": 60,
    "Road Trip": 90,
    "Favorites": 40
}
print("Workout duration:", playlist_durations["Workout"], "minutes")
playlist_durations["Party"] = 50
playlist_durations["Relax"] = 35
del playlist_durations["Study"]
print(playlist_durations)
```

## 2. Sets of food orders
```python
zomato_order_1 = {"Pizza", "Fries", "Cola"}
zomato_order_2 = {"Burger", "Fries", "Juice"}
print("Common items:", zomato_order_1.intersection(zomato_order_2))
print("All unique items:", zomato_order_1.union(zomato_order_2))
```

## 3. Instagram follower counts
```python
insta_followers = {"Aarav": 1200, "Diya": 450, "Kabir": 3000, "Mira": 800}
for username, followers in insta_followers.items():
    if followers > 1000:
        print(username, "has more than 1000 followers")
```
A dictionary stores key-value pairs. A set stores unique items and is useful for finding common or combined items.
