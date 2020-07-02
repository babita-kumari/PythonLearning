class Student:
    def __init__(self, one, two, three):
        self.one = one
        self.two = two
        self.three = three

    def sum(self):
        sum = self.one + self.two + self.three
        return sum


s1 = Student(5, 10, 12)
print(s1.sum())
