class Student:
    # Class attributes
    status = True
    pay = 1000
    
    def __init__(self, first_name, last_name, age, grades):
        # Instance attributes
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.grades = grades
    
    def get_full_name(self):
        """Returns first_name and last_name separated by space"""
        return f"{self.first_name} {self.last_name}"
    
    def get_discount(self):
        """If age < 18, reduce pay by 20%"""
        if self.age < 18:
            discount_amount = self.pay * 0.20
            self.pay -= discount_amount
            return self.pay
        return self.pay
    
    def calculate_average(self):
        """Returns average grade from grades list"""
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)
    
    def get_status(self):
        """Returns status based on average grade and updates status attribute if needed"""
        average = self.calculate_average()
        
        if average > 90:
            return "Excellent"
        elif 70 <= average <= 90:
            return "Good"
        elif 50 <= average < 70:
            return "Average"
        else:  # average < 50
            Student.status = False  # Update class attribute
            return "Poor"


# Example usage:
if __name__ == "__main__":
    # Create a student instance
    student1 = Student("გიორგი", "მაჩაბელი", 16, [95, 88, 92, 85])
    
    print(f"სახელი და გვარი: {student1.get_full_name()}")
    print(f"საშუალო ქულა: {student1.calculate_average()}")
    print(f"სტატუსი: {student1.get_status()}")
    print(f"გადასახადი: {student1.get_discount()}")
    
    # Create another student with poor grades
    student2 = Student("მარია", "ბერიძე", 19, [45, 40, 35])
    print(f"\nსტატუსი (Poor grade): {student2.get_status()}")
    print(f"Class status დაახლოვებული: {Student.status}")
