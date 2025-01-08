import json

courses = '{"name": "TommyTan", "language": ["Java", "Python"], "age": 32}'
dict_courses = json.loads(courses)
print(f"Json courses: {dict_courses}, \ntype: {type(dict_courses)}")

for k, v in dict_courses.items():
    print (f"Key: {k}, Value: {v}, type: {type(v)}")

print(f"Language [0]: {dict_courses['language'][0]}\n")

with open('test1.json', 'r') as file1:
    data1 = json.load(file1)
    print (f"Data: {data1}, \n  type {type(data1)}\n")
    for k, v in data1.items():
        print (f"Key: {k}, Value: {v} \n  type: {type(v)}")

    print('\n')
    print(f"Classifiers[0]: {data1['classifiers'][0]}")
    print(f"Extensions-Python Commands-Wrap Console-Chardetect: {data1['extensions']['python.commands']['wrap_console']['chardetect']}")
    # print(f"Products: {data['products']}\n")

    try:
        for product in data1['products']:
            if product['name'] == 'p3':
                print (f"p3 price: {product['price']}")
                assert product['price'] == 35
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except KeyError as e:
        print(f"KeyError: Missing key {e} in data.")
    except Exception as e:
        print(f"Unexpected error: {e}")

with open('test2.json', 'r') as file2:
    try:
        data2 = json.load(file2)
        print(f"Data1 equals Data2: {data1 == data2}")
        assert data1 == data2
    except AssertionError as e:
        print(f"AssertionError: {e}")