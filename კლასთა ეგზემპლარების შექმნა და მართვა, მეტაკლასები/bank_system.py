class BankAccount:
    """ბანკის ანგარიშის კლასი"""
    
    # კლასის ატრიბუტები
    bank_name = "Georgian Bank"
    __total_accounts = 0
    __next_account_number = 1
    
    def __init__(self, owner, balance):
        """
        ანგარიშის ინიციალიზაცია
        
        Args:
            owner (str): ანგარიშის მფლობელის სახელი
            balance (float): საწყისი ბალანსი
        """
        if not self.validate_amount(balance):
            raise ValueError("ბალანსი უნდა იყოს დადებითი რიცხვი")
        
        self._owner = owner  # protected ატრიბუტი
        self.__balance = balance  # private ატრიბუტი
        self.__account_number = self.__generate_account_number()
        
        # ანგარიშების რაოდენობის ზრდა
        BankAccount.__total_accounts += 1
    
    @staticmethod
    def __generate_account_number():
        """უნიკალური ანგარიშის ნომრის გენერირება"""
        account_num = f"AN{BankAccount.__next_account_number:04d}"
        BankAccount.__next_account_number += 1
        return account_num
    
    @staticmethod
    def validate_amount(amount):
        """
        თანხის ვალიდაცია
        
        Args:
            amount (float): შემოწმებული თანხა
            
        Returns:
            bool: True თუ თანხა დადებითია, False სხვაგვარად
        """
        try:
            return float(amount) > 0
        except (ValueError, TypeError):
            return False
    
    def deposit(self, amount):
        """
        ანგარიშზე თანხის დამატება
        
        Args:
            amount (float): დამატებული თანხა
            
        Returns:
            float: ახალი ბალანსი
        """
        if not self.validate_amount(amount):
            raise ValueError("დამატებული თანხა უნდა იყოს დადებითი რიცხვი")
        
        self.__balance += amount
        return self.__balance
    
    def withdraw(self, amount):
        """
        ანგარიშიდან თანხის გამოტანა
        
        Args:
            amount (float): გამოტანილი თანხა
            
        Returns:
            float: ახალი ბალანსი
        """
        if not self.validate_amount(amount):
            raise ValueError("გამოტანილი თანხა უნდა იყოს დადებითი რიცხვი")
        
        if amount > self.__balance:
            raise ValueError("საკმარისი თანხა ანგარიშზე არ არის")
        
        self.__balance -= amount
        return self.__balance
    
    def check_balance(self):
        """
        ბალანსის შემოწმება
        
        Returns:
            float: მიმდინარე ბალანსი
        """
        return self.__balance
    
    def get_account_number(self):
        """
        ანგარიშის ნომრის მიღება
        
        Returns:
            str: ანგარიშის ნომერი
        """
        return self.__account_number
    
    def change_owner(self, new_owner):
        """
        ანგარიშის მფლობელის შეცვლა
        
        Args:
            new_owner (str): ახალი მფლობელის სახელი
        """
        if not isinstance(new_owner, str) or not new_owner.strip():
            raise ValueError("მფლობელის სახელი უნდა იყოს არასაცარი სტრიქონი")
        
        self._owner = new_owner
    
    @classmethod
    def get_total_accounts(cls):
        """
        ხსნილი ანგარიშების მთლიანი რაოდენობის მიღება
        
        Returns:
            int: ანგარიშების რაოდენობა
        """
        return cls.__total_accounts
    
    def __str__(self):
        """ობიექტის სტრიქონიერი წარმოდგენა"""
        return f"Account: {self.__account_number} | Owner: {self._owner}"
    
    def __repr__(self):
        """ობიექტის წარმოდგენა თესლი"""
        return f"BankAccount(owner='{self._owner}', balance={self.__balance})"



if __name__ == "__main__":
    print("=== ბანკის სისტემის ტესტირება ===\n")
    
   
    account1 = BankAccount("ნინო ბერიძე", 1000)
    account2 = BankAccount("გია გელაშვილი", 5000)
    account3 = BankAccount("მარია კოსტავა", 3000)
    
   
    print("შექმნილი ანგარიშები:")
    print(account1)
    print(account2)
    print(account3)
    print()
    
   
    print(f"მთლიანი ანგარიშების რაოდენობა: {BankAccount.get_total_accounts()}\n")
    
  
    print(f"{account1.get_account_number()} ბალანსი: {account1.check_balance()} ლარი")
    
    
    account1.deposit(500)
    print(f"{account1.get_account_number()} ბალანსი (500 დამატების შემდეგ): {account1.check_balance()} ლარი")
    
   
    account1.withdraw(300)
    print(f"{account1.get_account_number()} ბალანსი (300 გამოტანის შემდეგ): {account1.check_balance()} ლარი\n")
    
  
    print(f"ძველი მფლობელი: {account2}")
    account2.change_owner("ალექსანდრე ჭანტურია")
    print(f"ახალი მფლობელი: {account2}\n")
    
  
    print("=== ვალიდაციის ტესტირება ===")
    print(f"validate_amount(100): {BankAccount.validate_amount(100)}")
    print(f"validate_amount(-50): {BankAccount.validate_amount(-50)}")
    print(f"validate_amount(0): {BankAccount.validate_amount(0)}")
    print(f"validate_amount('abc'): {BankAccount.validate_amount('abc')}")
    
   
    print("\n=== შეცდომის სცენარი ===")
    try:
        account1.withdraw(10000) 
    except ValueError as e:
        print(f"შეცდომა: {e}")
    
    try:
        account1.deposit(-100)  
    except ValueError as e:
        print(f"შეცდომა: {e}")
