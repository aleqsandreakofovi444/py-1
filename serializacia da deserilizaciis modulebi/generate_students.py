import json
import random
from faker import Faker

NUM_STUDENTS = 100
faker = Faker()
students = []

for i in range(1, NUM_STUDENTS + 1):
    student = {
        "student_id": i,
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "email": faker.email(),
        "age": random.randint(18, 70),
        "is_active": random.choice([True, False])
    }
    students.append(student)

with open("students.json", "w", encoding="utf-8") as f:
    json.dump(students, f, ensure_ascii=False, indent=2)

with open("students.json", "r", encoding="utf-8") as f:
    loaded_students = json.load(f)

active_students = [s for s in loaded_students if s["is_active"]]

with open("active_students.json", "w", encoding="utf-8") as f:
    json.dump(active_students, f, ensure_ascii=False, indent=2)
