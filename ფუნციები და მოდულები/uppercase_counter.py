def count_uppercase_and_convert(text):
    """
    დათვლის მაღალ რეგისტრში შეყვანილი სიმბოლოების რაოდენობას 
    და ტექსტს აკონვერტებს uppercase-ად.
    
    პარამეტრი:
        text (str): მომხმარებლის შეყვანილი ტექსტი
    
    დაბრუნებს:
        dict: {'uppercase_count': int, 'converted_text': str}
    
    მაგალითი:
        >>> count_uppercase_and_convert("Hello woRld")
        {'uppercase_count': 2, 'converted_text': 'HELLO WORLD'}
    """
    uppercase_count = sum(1 for char in text if char.isupper())
    converted_text = text.upper()
    
    return {
        'uppercase_count': uppercase_count,
        'converted_text': converted_text
    }


# თეთსაქმე ტესტი
if __name__ == "__main__":
    # ტესტი 1
    result1 = count_uppercase_and_convert("Hello woRld")
    print(f"ტექსტი: 'Hello woRld'")
    print(f"დიდი ასოების რაოდენობა: {result1['uppercase_count']}")
    print(f"აკონვერტებული ტექსტი: {result1['converted_text']}")
    print()
    
    # ტესტი 2
    result2 = count_uppercase_and_convert("Python Programming")
    print(f"ტექსტი: 'Python Programming'")
    print(f"დიდი ასოების რაოდენობა: {result2['uppercase_count']}")
    print(f"აკონვერტებული ტექსტი: {result2['converted_text']}")
    print()
    
    # ტესტი 3
    result3 = count_uppercase_and_convert("hello world")
    print(f"ტექსტი: 'hello world'")
    print(f"დიდი ასოების რაოდენობა: {result3['uppercase_count']}")
    print(f"აკონვერტებული ტექსტი: {result3['converted_text']}")
