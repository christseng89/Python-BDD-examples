from datetime import datetime
from calculator_class_demo import Calculator

class CalculatorInheritance(Calculator):
    # Additional Arithmetic Operations
    num2 = 11
    num3 = 2010

    first_num = 12
    second_num = 3

    def __init__(self):
        Calculator.__init__(self, self.first_num, self.second_num)

    def remainder(self):
        """Calculate modulus."""
        try:
            return self.a % self.b
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."

    def power(self):
        """Calculate power (a^b)."""
        return self.a ** self.b

    def sum (self):
        return self.a + self.b + self.add()

    def is_leap_year(self):
        """Check if a given year is a leap year."""
        try:
            year = self.num3 + self.a
            leapyear = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
            return leapyear
        except ValueError:
            return "Error: Invalid number."

obj = CalculatorInheritance()
print(f"Remainder = {obj.a} % {obj.b} = {obj.remainder()}")
print(f"Power = {obj.a} ** {obj.b} = {obj.power()}")
print(f"Sum: {obj.sum()} = {obj.a} + {obj.b} + {obj.add()}")
obj.is_leap_year()
print(f"Year {obj.num3} + {obj.a} = {obj.num3 + obj.a} is Leap year : {obj.is_leap_year()}")