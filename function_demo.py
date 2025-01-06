from datetime import datetime


def range_function_demo(num: int) -> None:
    for index in range(num):
        print (f"Range Function Demo with {num}, from 0, Index: {index}")
    print("\n")

range_function_demo(3)
range_function_demo(6)

def calculate_sum(numbers):
    total = 0
    for num in numbers:
        # Check if the item is int, float, or numeric string
        if isinstance(num, (int, float)):  # Numeric types
            total += num
        elif isinstance(num, str) and num.isdigit():  # Numeric string
            total += int(num)  # Convert to integer before addition
        # else:
        #     print(f"Warning: Skipping invalid value '{num}'")  # Handle non-numeric values
    return total

# Test the function
nums = [1, 2, '3', 4.5, 'five']  # Mixed list with integers, floats, and strings
result = calculate_sum(nums)
print(f"Calculate Sum: {result}")
print(f"Calculate Sum: {result}")
print('\n')

def get_greeting(current_hour):
    # Match case for time ranges
    match current_hour:
        case hour if 5 <= hour < 12:
            greeting = "Good Morning"
        case hour if 12 <= hour < 17:
            greeting =  "Good Afternoon"
        case hour if 17 <= hour < 21:
            greeting =  "Good Evening"
        case _:
            greeting = "Good Night"

    print(greeting + "\n")

get_greeting(datetime.now().hour)

def add_integer(a, b):
    return a + b

int1 = 3
int2 = 5
print(f"Add integer, {int1} + {int2} = {add_integer(int1, int2)}")