class MethodValidationMeta(type):
    """
    მეტაკლასი, რომელიც ვალიდაციას უკეთებს კლასის მეთოდების სახელებს.
    მეთოდი ვალიდური იქნება მხოლოდ თუ ის იწყება ქვედა ხაზით (_).
    """
    
    def __new__(mcs, name, bases, namespace):
        """
        მეტაკლასის შექმნა
        
        Args:
            name (str): კლასის სახელი
            bases (tuple): მშობელი კლასები
            namespace (dict): კლასის namespace
            
        Raises:
            ValueError: თუ მეთოდი არ იწყება უტა ხაზით
        """
        
        
        for attr_name, attr_value in namespace.items():
           
            if callable(attr_value) and not isinstance(attr_value, type):
               
                if not attr_name.startswith('_'):
                    raise ValueError(
                        f"მეთოდი '{attr_name}' არ არის ვალიდური. "
                        f"ყველა მეთოდი უნდა იწყებოდეს ქვედა ხაზით (_). "
                        f"მაგ: _{attr_name}()"
                    )
        
        return super().__new__(mcs, name, bases, namespace)



class ValidClass(metaclass=MethodValidationMeta):
    """კლასი, რომელიც იყენებს MethodValidationMeta მეტაკლასს"""
    
    def __init__(self):
        self.value = 10
    
    def _private_method(self):
        """პირადი მეთოდი"""
        return self.value * 2
    
    def _another_private(self):
        """კიდევ ერთი პირადი მეთოდი"""
        return self.value + 5
    
    @staticmethod
    def _static_method():
        """სტატიკური მეთოდი"""
        return "სტატიკური"
    
    @classmethod
    def _class_method(cls):
        """კლასის მეთოდი"""
        return f"კლასი: {cls.__name__}"



try:
    class InvalidClass(metaclass=MethodValidationMeta):
        """ეს კლასი გამოიწვევს ValueError-ს"""
        
        def public_method(self):  
            return "public"
except ValueError as e:
    print(f" კლასის შექმნა ვერ მოხერხდა:\n   {e}\n")



print("=== ვალიდური კლასის ტესტირება ===\n")

obj = ValidClass()
print(f"✓ ValidClass წარმატებით შეიქმნა")
print(f"✓ _private_method(): {obj._private_method()}")
print(f"✓ _another_private(): {obj._another_private()}")
print(f"✓ _static_method(): {ValidClass._static_method()}")
print(f"✓ _class_method(): {ValidClass._class_method()}\n")


print("=== არასწორი კლასის მცდელობა ===\n")

try:
    class AnotherInvalidClass(metaclass=MethodValidationMeta):
        """კიდევ ერთი არასწორი კლასი"""
        
        def _valid_method(self):
            return "valid"
        
        def invalid_method(self):  
            return "invalid"
            
except ValueError as e:
    print(f" კლასის შექმნა ვერ მოხერხდა:\n   {e}\n")



class ClassWithAttributes(metaclass=MethodValidationMeta):
    """ატრიბუტები არ იწვევენ შეცდომას, მხოლოდ მეთოდები"""
    
    public_attribute = "ეს არის ატრიბუტი"  
    _private_attribute = 42  
    
    def _method(self):
        """კლასი შეიქმნა წარმატებით, რადგან მეთოდი იწყება _-ით"""
        return self.public_attribute


print(" კლასი წარმატებით შეიქმნა (ატრიბუტები არ აღზევენ შეცდომას)")
obj2 = ClassWithAttributes()
print(f" obj2._method(): {obj2._method()}\n")

print("=== დასკვნა ===")
print(" მეტაკლასი ნორმალურად მუშაობს!")
print(" მხოლოდ უტა-ხაზიანი მეთოდები მოწვევილია")
print(" ატრიბუტები არ შემოწმდებიან")
