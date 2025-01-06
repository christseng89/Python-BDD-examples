from datetime import datetime, timedelta
import math  # For rounding up

class Calculator:
    num1 = 10
    # Constructor for arithmetic operations
    def __init__(self, a=0.0, b=0.0):
        self.a = a
        self.b = b

    # Arithmetic Operations
    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        try:
            return self.a / self.b
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."

    # Date Operations
    @staticmethod
    def subtract_dates_in_days(date1:datetime, date2:datetime):
        """Calculate the difference in days between two dates."""
        try:
            d1 = datetime.strptime(date1, "%Y-%m-%d")
            d2 = datetime.strptime(date2, "%Y-%m-%d")
            delta = abs((d1 - d2).days)
            return f"Difference: {delta} day(s)"
        except ValueError:
            return "Error: Invalid date format. Use 'YYYY-MM-DD'."

    @staticmethod
    def subtract_dates_in_months(date1, date2):
        """Calculate the difference in months (round up partial months)."""
        try:
            # Parse dates
            d1 = datetime.strptime(date1, "%Y-%m-%d")
            d2 = datetime.strptime(date2, "%Y-%m-%d")

            # Ensure d1 is earlier than d2
            if d1 > d2:
                d1, d2 = d2, d1

            # Calculate year and month difference
            year_diff = d2.year - d1.year
            month_diff = d2.month - d1.month
            day_diff = d2.day - d1.day

            # Total months
            total_months = (year_diff * 12) + month_diff

            # Round up if there are remaining days
            if day_diff > 0:
                total_months += 1

            return f"Difference: {total_months} month(s)"
        except ValueError:
            return "Error: Invalid date format. Use 'YYYY-MM-DD'."

    @staticmethod
    def subtract_dates_in_quarters(date1, date2):
        """Calculate the difference in quarters (round up partial quarters)."""
        try:
            # Parse dates
            d1 = datetime.strptime(date1, "%Y-%m-%d")
            d2 = datetime.strptime(date2, "%Y-%m-%d")

            # Ensure d1 is earlier than d2
            if d1 > d2:
                d1, d2 = d2, d1

            # Calculate year, month, and day difference
            year_diff = d2.year - d1.year
            month_diff = d2.month - d1.month
            day_diff = d2.day - d1.day

            # Total months
            total_months = (year_diff * 12) + month_diff

            # Convert months to quarters and round up
            total_quarters = math.ceil(total_months / 3)

            # Adjust for remaining days if needed
            if day_diff > 0 and (total_months % 3) != 0:
                total_quarters += 1

            return f"Difference: {total_quarters} quarter(s)"
        except ValueError:
            return "Error: Invalid date format. Use 'YYYY-MM-DD'."

    @staticmethod
    def add_days_to_date(date, days):
        """Add days to a given date."""
        try:
            d = datetime.strptime(date, "%Y-%m-%d")
            new_date = d + timedelta(days=days)
            return new_date.strftime("%Y-%m-%d")
        except ValueError:
            return "Error: Invalid date format. Use 'YYYY-MM-DD'."


# Example Usage
if __name__ == "__main__":
    # Arithmetic operations
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    #
    calc = Calculator(num1, num2)
    print(f"Addition: {calc.add()}")
    print(f"Subtraction: {calc.subtract()}")
    print(f"Multiplication: {calc.multiply()}")
    print(f"Division: {calc.divide()}")

    # Date operations
    print("\nDate Operations:")
    date1 = input("Enter first date (YYYY-MM-DD): ")
    date2 = input("Enter second date (YYYY-MM-DD): ")

    # Calculate differences in days, months, and quarters
    print(Calculator.subtract_dates_in_days(date1, date2))      # Days
    print(Calculator.subtract_dates_in_months(date1, date2))    # Months (rounded up)
    print(Calculator.subtract_dates_in_quarters(date1, date2))  # Quarters (rounded up)

    # Add days to a date
    base_date = input("\nEnter base date (YYYY-MM-DD): ")
    days_to_add = int(input("Enter number of days to add: "))
    print(f"New Date: {Calculator.add_days_to_date(base_date, days_to_add)}")
