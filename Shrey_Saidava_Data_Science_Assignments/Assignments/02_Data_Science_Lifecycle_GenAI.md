# Assignment 1.2 — Data Science Lifecycle and Generative AI
**Name:** Shrey Saidava | **Course:** Data Science

## 1. Business problem
I choose a food-delivery app. The problem is that users may leave the app when delivery takes too long. The goal is to predict delays and show a more realistic delivery time before the user places an order.

## 2. Ways to collect data
1. **API:** request permitted data from an app or service through its API.
2. **Survey:** ask users about their experience.
3. **Web scraping:** collect publicly available webpage information only when the site’s rules and permissions allow it.

## 3. Clean a sample dataset
```python
import pandas as pd

data = {
    "restaurant": ["Pizza Hub", None, "BURGER POINT", "Cafe One"],
    "orders": [12, 8, None, 15]
}
df = pd.DataFrame(data)
df = df.dropna().copy()          # remove rows with missing values
df["restaurant"] = df["restaurant"].str.lower()
print(df)
```

## 4. Simple data exploration
```python
print(df.head())
print(df.info())
print(df.describe(numeric_only=True))
print(df.isnull().sum())
```
These commands show sample rows, column types, numeric summaries, and missing values.

## 5. Use of a GenAI tool
I can ask a GenAI tool to suggest questions for exploring delivery data, explain Python errors, or help draft code. I should check the output, test the code, and avoid sharing private customer information.
