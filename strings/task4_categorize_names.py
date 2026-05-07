# Task 4: სახელების კატეგორიზაცია (გრძელი და მოკლე სახელები)
long_names = []
short_names = []

print("უსასრულო სახელების შეყვანის რეჟიმი")
print("დაწერეთ 'stop', 'exit' ან 'quit' რეჟიმის დასახურებლად (ციფრული მნიშვნელობა არ აკრებს)\n")

while True:
    # მომხმარებელი შემოიყვანს სახელს
    user_input = input("დაწერეთ სახელი: ")
    
    # თავსა და ბოლოში მოაშორეთ ცარიელი ადგილები
    user_input = user_input.strip()
    
    # შეამოწმეთ, თუ მომხმარებელი სასტესი სიტყვა შეიყვანა
    if user_input.lower() in ['stop', 'exit', 'quit']:
        print("პროგრამა დახურულია!")
        break
    
    # თუ დაცემულ ადგილი აღმოჩნდა, გაიტანეთ ყურადღება
    if user_input == "":
        print("გთხოვთ, დაწერეთ ვალიდური სახელი!\n")
        continue
    
    # პირველი ასო დიდი გახადე, დანარჩენი პატარა
    formatted_name = user_input.capitalize()
    
    # სახელის სიგრძე განხორციელდება
    if len(formatted_name) > 3:
        long_names.append(formatted_name)
        print(f"✓ '{formatted_name}' დაემატა გრძელ სახელებში\n")
    else:
        short_names.append(formatted_name)
        print(f"✓ '{formatted_name}' დაემატა მოკლე სახელებში\n")

# ბეჭდი ლისტები
print("\n" + "="*40)
print("გრძელი სახელები (3-ზე მეტი ასო):")
print(long_names)
print("\nმოკლე სახელები (3 ასო ან ნაკლები):")
print(short_names)
