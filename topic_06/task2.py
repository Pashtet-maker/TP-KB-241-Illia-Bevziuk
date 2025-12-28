students = [
    {"name": "Emma", "grade": 10},
    {"name": "Bob",  "grade": 45},
    {"name": "Zak",  "grade": 50},
    {"name": "Jon",  "grade": 33}
]

sorted_by_name = sorted(students, key=lambda x: x["name"])
print("Сортування за ім'ям:")
for s in sorted_by_name:
    print(s)

sorted_by_grade = sorted(students, key=lambda x: x["grade"])
print("\nСортування за оцінкою:")
for s in sorted_by_grade:
    print(s)