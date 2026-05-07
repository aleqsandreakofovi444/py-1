# Task 2: ლისტიდან უნიკალური ელემენტების ფილტრაცია (set გარეშე)
original_list = ['a', 'b', 2, 4, 2, 'c', 'j', 1, 'b', 'd', 'c', 4, 1]
unique_list = []

# თითოეული ელემენტი ვამოწმებთ თუ უკვე ამ ლისტში დაემატა თუ არა
for element in original_list:
    # ვიტყოდებით: თუ ელემენტი გამოჩნდა უნიკალურ ლისტში? კი / არა
    is_found = False
    for unique_element in unique_list:
        if element == unique_element:
            is_found = True
            break
    
    # თუ ელემენტი არ დაემატა, დაამატებთ
    if not is_found:
        unique_list.append(element)

print("ორიგინალური ლისტი:", original_list)
print("უნიკალური ელემენტებით:", unique_list)
