str1 = "Udemy.com"
print (f"str1[0:3]: {str1[0:3]}")
print(f"str1[-3:]: {str1[-3:]}")
print('\n')
words = str1.split('.')
print(words)

str1 = "Python is a powerful language"

# Split the string by spaces
words = str1.split() 

print(f"Split to Words: {words}")

str2 = ' '.join(words)
print (f"Join Words to String: {str2}")

print (f"Compare 2 strings: {str1 == str2}")
print (f"String1 contains Python: {str1.__contains__('Python')}")
print (f"Python in String1: {'Python' in str1}")
print (f"String1 upper case: {str1.upper()}")
print ('\n')

print (' great '.strip())
print (' great '.lstrip())
print (' great '.rstrip())