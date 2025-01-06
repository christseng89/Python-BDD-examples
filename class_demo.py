class Demo:
    num0 = 100

    def get_data(self) -> None:
        print (f"Executing get_data in Class with num0: {self.num0}, self.a: {self.num1}, self.b: {self.num2}")

    def __init__(self, a=0.0, b=0.0):
        self.num1 = a
        self.num2 = b

        print (f"Executing constructor when object is created with num0: {self.num0}, a: {a}, b: {b}")

    def sum_data(self):
        return self.num1 + self.num2 + Demo.num0 + self.num0

demo = Demo(2, 3)
print('***********\n')

demo.get_data()
print(f"Num0: {demo.num0}")
print(f"Sum_data: {demo.sum_data()}")
