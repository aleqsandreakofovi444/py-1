# პროგრამა 3: ანაგრამის შემოწმება (sorted() ფუნქციის გარეშე)

word1 = input("შეიყვანეთ პირველი სიტყვა: ").lower()
word2 = input("შეიყვანეთ მეორე სიტყვა: ").lower()

# ორივე სიტყვის სიგრძე უნდა იყოს ერთი
if len(word1) != len(word2):
    print("არ არის ანაგრამა - სიტყვების სიგრძე განსხვავებული")
else:
    # ითვლით თითოეული ასოს რაოდენობას პირველ სიტყვაში
    char_count = {}
    for char in word1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # შეამოწმით მეორე სიტყვის ასოები
    is_anagram = True
    for char in word2:
        if char not in char_count or char_count[char] == 0:
            is_anagram = False
            break
        else:
            char_count[char] -= 1
    
    # თუ დარჩა რაიმე ასო, მაშინ არ არის ანაგრამა
    if is_anagram:
        for count in char_count.values():
            if count != 0:
                is_anagram = False
                break
    
    if is_anagram:
        print("კი, ეს ორი სიტყვა ერთმანეთის ანაგრამაა!")
    else:
        print("არა, ეს ორი სიტყვა ერთმანეთის ანაგრამა არ არის")
