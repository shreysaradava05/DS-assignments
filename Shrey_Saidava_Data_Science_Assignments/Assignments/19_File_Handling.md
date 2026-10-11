# Assignment 2.12 — File Handling (Text, CSV and JSON)
**Name:** Shrey Saidava | **Course:** Data Science

## 1. Write and read a text file
```python
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("My first Data Science file.\n")

with open("notes.txt", "r", encoding="utf-8") as file:
    print(file.read())
```

## 2. Write and read a CSV file
```python
import csv

rows = [["name", "marks"], ["Aarav", 85], ["Diya", 92]]
with open("marks.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(rows)

with open("marks.csv", "r", newline="", encoding="utf-8") as file:
    for row in csv.reader(file):
        print(row)
```

## 3. Save data as JSON
```python
import json
student = {"name": "Shrey Saidava", "course": "Data Science"}
with open("student.json", "w", encoding="utf-8") as file:
    json.dump(student, file, indent=4)
with open("student.json", "r", encoding="utf-8") as file:
    print(json.load(file))
```
`with open()` closes the file automatically. CSV is useful for table-shaped data, and JSON is useful for structured key-value data.
