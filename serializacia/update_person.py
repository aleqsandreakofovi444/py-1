class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person: ({self.name}, {self.age})"


def serialize(person):
    """Person ობიექტი სტრიქონად"""
    return f"Name: {person.name}, Age: {person.age}"


def deserialize(line):
    """სტრიქონი Person ობიექტად"""
    parts = line.split(", ")
    name = parts[0].split(": ")[1]
    age = int(parts[1].split(": ")[1])
    return Person(name, age)



p = Person("Alexander", 16)
with open("person_data.txt", 'w', encoding='utf-8') as f:
    f.write(serialize(p))

print(f"✓ ფაილი განახლდა: {serialize(p)}")
