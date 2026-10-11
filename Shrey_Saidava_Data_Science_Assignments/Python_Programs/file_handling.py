import csv
import json

with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("My first Data Science file.\n")
with open("notes.txt", "r", encoding="utf-8") as file:
    print(file.read())

with open("marks.csv", "w", newline="", encoding="utf-8") as file:
    csv.writer(file).writerows([["name", "marks"], ["Aarav", 85], ["Diya", 92]])

student = {"name": "Shrey Saidava", "course": "Data Science"}
with open("student.json", "w", encoding="utf-8") as file:
    json.dump(student, file, indent=4)
print("Files created successfully")
