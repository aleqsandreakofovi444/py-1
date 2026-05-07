# პროგრამა 1: სიტყვის ჩანაცვლება წინადადებაში

sentence = input("შეიყვანეთ წინადადება: ")
first_word = input("შეიყვანეთ პირველი სიტყვა (რომელი უნდა ჩაანაცვლოს): ")
second_word = input("შეიყვანეთ მეორე სიტყვა (რომელი უნდა ჩაანაცვლოს): ")

# სიტყვის ჩანაცვლება
new_sentence = sentence.replace(first_word, second_word)

print("შედეგი:", new_sentence)
