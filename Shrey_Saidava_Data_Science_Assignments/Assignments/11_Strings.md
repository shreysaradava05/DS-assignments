# Assignment 2.4 — Strings
**Name:** Shrey Saidava | **Course:** Data Science

```python
text = "  pizza-BURGER-pasta  "
clean_text = text.strip().lower().replace("-", " ")
print(clean_text)

features = "recommendations-search-download-share"
for feature in features.split("-"):
    print(feature)
```
`strip()` removes spaces at the start and end. `lower()` makes letters lowercase. `replace()` changes hyphens to spaces. `split()` separates a string into parts.
