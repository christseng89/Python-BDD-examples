from datetime import datetime
# from decimal import Decimal

# Get the current hour
current_hour = datetime.now().hour
print(f"Current Hour: {current_hour}")

def get_greeting():
    # Determine the greeting based on the time of day
    if 5 <= current_hour < 12:
        return "Good Morning"
    elif 12 <= current_hour < 17:
        return "Good Afternoon"
    elif 17 <= current_hour < 21:
        return "Good Evening"
    else:
        return "Good Night"

# Display the greeting
greeting = get_greeting()
print(f"{greeting}! Current Hour: {current_hour}, Welcome = If Else!\n")

def get_greeting():
    # Match case for time ranges
    match current_hour:
        case hour if 5 <= hour < 12:
            return "Good Morning"
        case hour if 12 <= hour < 17:
            return "Good Afternoon"
        case hour if 17 <= hour < 21:
            return "Good Evening"
        case _:
            return "Good Night"

# Display the greeting
greeting = get_greeting()
print(f"{greeting}! Current Hour: {current_hour}, Welcome = Match Case!")

# Loop
list_a = ['hey', 'you', 'aaa', 1, 3, 12, 1.2, 'go']
index = 0
summation = 0.0
for item in list_a:
    print(f"Index {index} - in: {item}")

    if isinstance(item, (int, float)):
        summation += item  # Add numeric values to the sum
    index += 1  # Increment index
print(f"\nSummation: {summation}\n")

index = 0
while index < len(list_a):
    print(f"Index {index} - while: {list_a[index]}")
    index += 1
print("\n")

for index, item in enumerate(list_a):
    print(f"Index {index} - enumerate: {item}")
print("\n")

summation = 0
for index in range(1, 6):
    summation += index
    print (f"Index - range: {index}")
print(f"\nSummation: {summation}\n")

for index in range(1, 10, 2):
    print (f"Index - range, skip 2: {index}")
print("\n")

for index in range(6):
    print (f"Index - range, start from 0: {index}")
print("\n")

# While
index = 4
while index > 0:
    if index != 3:
        print(f"Index - while: {index}")
    index -= 1
print("\n")

index = 10
while index > 0:
    if index == 6:
        index -= 1
        continue
    if index == 3:
        break
    print(f"Index - while/continue/break: {index}")
    index -= 1

