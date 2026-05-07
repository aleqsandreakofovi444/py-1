# პროგრამა 2: ყველაზე გრძელი სიტყვა (max() ფუნქციის გარეშე)

sentence = input("შეიყვანეთ წინადადება: ")

# წინადადება სიტყვებად გავყოთ
words = sentence.split()

if len(words) == 0:
    print("წინადადება ცარიელია!")
else:
    # ყველაზე გრძელი სიტყვის პოვნა ციკლის საშუალებით
    longest_word = words[0]
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    
    print("ყველაზე გრძელი სიტყვა:", longest_word)
    print("მისი სიგრძე:", len(longest_word))
