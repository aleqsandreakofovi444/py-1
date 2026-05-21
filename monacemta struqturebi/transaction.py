def commission_decorator(func):
    """
    დეკორატორი, რომელიც საკომისიოს (1 ლარი) ჩამოაჭრის ტრანზაქციის ოდენობიდან
    """
    def wrapper(balance, amount):
        commission = 1  # საკომისიო 1 ლარი
        total_needed = amount + commission
        
        # თუ საკმარისი თანხა არ იქნება ანგარიშზე, დაბრუნებულია შეცდომის ტექსტი
        if balance < total_needed:
            return f"შეცდომა: საკმარისი თანხა არ იქნება. საჭიროა {total_needed} ლარი, ხოლო ანგარიშზე {balance} ლარია."
        
        # თუ კი, გამოიძახება ფუნქცია
        return func(balance, total_needed)
    
    return wrapper


@commission_decorator
def transaction(balance, amount):
    """
    ტრანზაქცია - ბალანსიდან გამოაკლებს გადასახდელ თანხას (თანხა + საკომისიო)
    
    Args:
        balance: ანგარიშზე არსებული თანხა
        amount: გადასახდელი თანხა (საკომისიოთან ერთად)
    
    Returns:
        ახალი ბალანსი
    """
    new_balance = balance - amount
    return new_balance


# ტესტირება
if __name__ == "__main__":
    # ტესტი 1: საკმარისი თანხა
    print("ტესტი 1:")
    result = transaction(100, 50)
    print(f"ბალანსი: 100, გადასახდელი: 50")
    print(f"ახალი ბალანსი: {result}\n")
    
    # ტესტი 2: საკმარისი თანხა
    print("ტესტი 2:")
    result = transaction(60, 50)
    print(f"ბალანსი: 60, გადასახდელი: 50")
    print(f"ახალი ბალანსი: {result}\n")
    
    # ტესტი 3: საკმარისი თანხა არ იქნება
    print("ტესტი 3:")
    result = transaction(30, 50)
    print(f"ბალანსი: 30, გადასახდელი: 50")
    print(f"შედეგი: {result}\n")
