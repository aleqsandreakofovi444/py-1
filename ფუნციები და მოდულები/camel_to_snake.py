import re


def camel_case_to_snake_case(camel_case_str):
    """
    camelCase ცვლადებს გადააქცევს snake_case სახით.
    
    პარამეტრი:
        camel_case_str (str): camelCase ფორმატში ცვლადი
    
    დაბრუნებს:
        str: snake_case ფორმატში გადაქცეული ცვლადი
    
    მაგალითი:
        >>> camel_case_to_snake_case("firstName")
        'first_name'
        >>> camel_case_to_snake_case("preferredFirstName")
        'preferred_first_name'
    """
    # ჩავამატოთ underscore დიდი ასოს წინ (მაგრამ არა სტრიქის დასაწყისში)
    snake_case_str = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_case_str)
    # გადავაქციოთ lowercase-ად
    return snake_case_str.lower()


# თეთსაქმე ტესტი
if __name__ == "__main__":
    test_cases = [
        "firstName",
        "name",
        "preferredFirstName",
        "lastName",
        "phoneNumber",
        "isActive",
        "getUserData",
        "getUserDataFromDatabase",
        "a",
        "ABC"
    ]
    
    print("camelCase → snake_case კონვერტაცია:\n")
    for test in test_cases:
        result = camel_case_to_snake_case(test)
        print(f"{test:25} → {result}")
