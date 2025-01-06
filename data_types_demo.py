print ("Hello World")

# https://www.digitalocean.com/community/tutorials/python-data-types
dict_c, tuple_b, Str = 3, 2.3, 'abc'

print (dict_c, Str)
print (f"Value a: {dict_c}, b: {tuple_b}, Str: {Str}")
print (f"Type a: {type(dict_c)}, b: {type(tuple_b)}, Str: {type(Str)}")
print("\n")

# List ...
list_a = ["hey", "you", 1, 2, 3, "go"]
print(f"list_a[2]: {list_a[2]}, list_a[-1]: {list_a[-1]}, list_a[0:2]: {list_a[0:2]}, type list_a: {type(list_a)}")
list_a.insert(2, 'aaa')
list_a.append('END')
print(f"list_a after insert: {list_a}")
del list_a[-1]
print(f"list_a after delete: {list_a}")
print("\n")

# Tuple
tuple_b=("hello", 1,2,3,4,"go", {"dic1": 123})
print(f"tuple_b[2]: {tuple_b[2]}, tuple_b[-2]: {tuple_b[-2]}, tuple_b[0:2]: {tuple_b[0:2]}, type tuple_b: {type(tuple_b)}")
print(f"type tuple_b[6]: {type(tuple_b[6])}")

b_list = list(tuple_b)                # Convert tuple to list
b_list.insert(2, "aaa")
b_list.append('END')# Insert "aaa" at index 3
tuple_b = tuple(b_list)               # Convert back to tuple
print(f"tuple_b after insert: {tuple_b}")

del b_list[-1]
tuple_b = tuple(b_list)
print(f"tuple_b after delete: {tuple_b}")

# Update element
tuple_b[7]['dic1'] = 456
tuple_b = tuple_b[:4] + (33,) + tuple_b[5:]

# Add element
tuple_b = ("start",) + tuple_b
# Add element in the middle
tuple_b = tuple_b[:4] + ("middle",) + tuple_b[4:]

print(f"tuple_b after add/update: {tuple_b}")

print("\n")

# Dictionary
dict_c = {1: "first name", 2: "last name", "gender": "male" , "age":33, "age": 12}

print(f"dict_c['age']: {dict_c['age']}, dict_c[2]: {dict_c[2]}, list(dict_c)[0:2], {list(dict_c)[0:2]}, type dict_c: {type(dict_c)}")
a_list = list(dict_c.items())
a_list.insert(2, (3, "aaa"))
a_list.append(('END', 'end'))
dict_c=dict(a_list)
print(f"dict_c after insert: {dict_c}")

del a_list[-1]  # Removes the first key-value pair (1, "first name")
dict_c = dict(a_list)
print(f"dict_c after delete: {dict_c}")

dict_c[1] = "Jeff"
dict_c[2] = "Wang"
dict_c['age'] = 37

dict_c["new1"] = "Eric"
dict_c["new2"] = "Zeng"

print(f"dict_c after add & update: {dict_c}")
