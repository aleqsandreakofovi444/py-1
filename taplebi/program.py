# Task 1: Interactive person lookup
def task1():
    persons = [
        ('Kelly', 'Simpson', 26),
        ('Erika', 'Stephens', 24),
        ('Cheryl', 'Dunn', 30),
        ('Amy', 'Larsen', 49),
        ('Christine', 'Gordon', 23),
        ('Monica', 'Huff', 38),
        ('David', 'Nixon', 36),
        ('Cindy', 'Escobar', 41),
        ('Cindy', 'White', 33), 
        ('Joel', 'Hall', 43),
        ('Steven', 'Winters', 28),
        ('Alex', 'Cole', 68),
        ('Alex', 'Smith', 32),
        ('Brittany', 'Thompson', 18),
        ('Ernest', 'Young', 43),
        ('Traci', 'Wells', 38),
        ('Andrew', 'Flores', 61),
        ('Christopher', 'Lewis', 29),
        ('Kevin', 'Willis', 57),
        ('Kayla', 'Lucas', 28),
        ('Michelle', 'Rush', 43),
        ('Thomas', 'Mason', 37)
    ]
    
    while True:
        name = input("შეიყვანეთ სახელი (ან 'stop' გასასრულებლად): ").strip()
        
        if name.lower() == "stop":
            print("პროგრამა დასრულდა!")
            break
        
        # Find all people with this name
        matching_people = [person for person in persons if person[0] == name]
        
        if not matching_people:
            print(f"სახელი '{name}' არ იქნა მოძებნილი სიაში!")
            continue
        
        # If multiple people with same name, ask for last name
        if len(matching_people) > 1:
            lastname = input(f"იპოვე რამდენიმე '{name}' დაკომპილაციო. შეიყვანეთ გვარი: ").strip()
            
            # Find person with both matching name and lastname
            person = None
            for p in matching_people:
                if p[1] == lastname:
                    person = p
                    break
            
            if person:
                print(f"{person[0]} {person[1]}-ის ასაკი: {person[2]} წელი")
            else:
                print(f"გვარი '{lastname}' არ იქნა მოძებნილი '{name}'-ის ქვეშ!")
        else:
            # Only one person with this name
            person = matching_people[0]
            print(f"{person[0]} {person[1]}-ის ასაკი: {person[2]} წელი")
        
        print()


# Task 2: Set operations on words
def task2():
    word1 = input("შეიყვანეთ პირველი სიტყვა: ").strip().lower()
    word2 = input("შეიყვანეთ მეორე სიტყვა: ").strip().lower()
    
    # Convert words to sets of characters
    set1 = set(word1)
    set2 = set(word2)
    
    # Common characters (intersection)
    common = set1 & set2
    
    # Different characters (symmetric difference)
    different = set1 ^ set2
    
    # Combined characters (union)
    combined = set1 | set2
    
    print(f"\nპირველი სიტყვის სიმბოლოები: {set1}")
    print(f"მეორე სიტყვის სიმბოლოები: {set2}")
    print(f"\nსაერთო სიმბოლოები: {common}")
    print(f"განსხვავებული სიმბოლოები: {different}")
    print(f"გაერთიანებული სიმბოლოები (ორივე ერთად): {combined}")


# Main menu
if __name__ == "__main__":
    while True:
        print("\n--- თავი გვერდი ---")
        print("1. დავალება 1: პირის ასაკის ძებნა")
        print("2. დავალება 2: სიტყვების სიმბოლოების ანალიზი")
        print("3. გამოსვლა")
        
        choice = input("აირჩიეთ ვარიანტი (1, 2, ან 3): ").strip()
        
        if choice == "1":
            print("\n--- დავალება 1 ---")
            task1()
        elif choice == "2":
            print("\n--- დავალება 2 ---")
            task2()
        elif choice == "3":
            print("გამოდით!")
            break
        else:
            print("უცნობი ვარიანტი. სცადეთ ხელახლა!")
