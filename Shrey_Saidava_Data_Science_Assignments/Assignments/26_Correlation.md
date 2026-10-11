# Assignment 5.7 — Correlation
**Name:** Shrey Saidava | **Course:** Data Science

## 1. Meaning
Correlation measures how two variables change together. Positive correlation means both tend to rise together; negative correlation means one tends to rise when the other falls; near-zero correlation means there is little linear relationship.

## 2. Example using app data
```python
import numpy as np

study_hours = [1, 2, 3, 4, 5]
quiz_marks = [45, 50, 65, 70, 85]
print("Correlation:", np.corrcoef(study_hours, quiz_marks)[0, 1])
```
This small example is expected to show positive correlation between study hours and quiz marks.

## 3. Delivery example
A food-delivery app might find a positive correlation between the number of available delivery partners and the number of orders completed. However, correlation does not prove that one variable causes the other. Time of day, weather, and promotions could also affect orders.
