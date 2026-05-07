data_list = []

while True:
    name = input("input name: ")
    
    if name.lower() == "stop" or name.lower() == "exit":
        break
    
    age = input("input age: ")
    profession = input("input profession: ")
    
    data_list.append({"name": name, "age": int(age), "profession": profession})

print(data_list)
