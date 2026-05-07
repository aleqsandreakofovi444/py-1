"""
სამი პროგრამული ფუნქცია
Three programming functions
"""


def sum_user_input(times=None):
    """
    პარამეტრად მიიღებს რამდენჯერ უნდა ჰკითხოს მომხმარებელს რიცხვი.
    თუ არგუმენტად არ გადაეცა რიცხვი, ფუნქცია 5-ჯერ ჰკითხავს მომხმარებელს
    და დააბრუნებს ყველა შეყვანილი რიცხვის ჯამს.
    
    Takes as parameter how many times to ask the user for a number.
    If no argument is provided, asks 5 times and returns the sum.
    """
    if times is None:
        times = 5
    
    total = 0
    for i in range(times):
        try:
            number = float(input(f"შეიყვანეთ რიცხვი {i+1}: "))
            total += number
        except ValueError:
            print("შეცდომა! გთხოვთ შეიყვანეთ ვალიდური რიცხვი")
            i -= 1
    
    return total



def separate_odd_even(*args):
    """
    მიიღებს არგუმენტების განუსაზღვრელ რაოდენობას მთელი რიცხვების სახით
    და დააბრუნებს ორ ლისტს: პირველი ლისტი კენტი რიცხვებით,
    მეორე ლისტი ლუწი რიცხვებით.
    
    Takes an undefined number of integer arguments and returns two lists:
    first list with odd numbers, second list with even numbers.
    """
    odd_numbers = []
    even_numbers = []
    
    for num in args:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    
    return odd_numbers, even_numbers



def count_words(sentence):
    """
    პარამეტრად მიიღებს მომხმარებლის მიერ შეყვანილ წინადადებას
    და დააბრუნებს დიქტს, სადაც თითოეული სიტყვა და მისი რაოდენობა.
    დიდ და პატარა ასოებს მნიშვნელობა არ აქვს (case insensitive).
    
    Takes a sentence and returns a dictionary with word counts.
    Case insensitive - uppercase and lowercase letters don't matter.
    """
    import string
    
   
    sentence_lower = sentence.lower()
    
   
    sentence_clean = sentence_lower.translate(str.maketrans('', '', string.punctuation))
    
    
    words = sentence_clean.split()
    
   
    word_count = {}
    for word in words:
        if word:  # თუ სიტყვა ცარიელი არ არის
            word_count[word] = word_count.get(word, 0) + 1
    
    return word_count



if __name__ == "__main__":
    print("=" * 50)
    print("ფუნქცია 1: რიცხვების შეკრება")
    print("=" * 50)
    # result1 = sum_user_input()  # 5-ჯერ ჰკითხავს
    # print(f"ჯამი: {result1}")
    print("(კომენტარი გასაწერი - ხელმისაწვდომი კოდი მოთხოვნისას)")
    
    print("\n" + "=" * 50)
    print("ფუნქცია 2: კენტი და ლუწი რიცხვები")
    print("=" * 50)
    odd, even = separate_odd_even(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(f"კენტი რიცხვები: {odd}")
    print(f"ლუწი რიცხვები: {even}")
    
    print("\n" + "=" * 50)
    print("ფუნქცია 3: სიტყვების დათვლა")
    print("=" * 50)
    sentence = "This is a test. This test is fun."
    word_counts = count_words(sentence)
    print(f"წინადადება: {sentence}")
    print(f"სიტყვების რაოდენობა: {word_counts}")
