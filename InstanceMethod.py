# Create Class
class Student:
    school = 'Krishna'

    # _init method
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def add(self):
        return self.m1 + self.m2 + self.m3

    #  avg method
    def avg_add(self):
        return (self.m1 + self.m2 + self.m3) / 3, self.m1 + self.m2 + self.m3

    def get_m1(self):
        return self.m1

    def set_m2(self, value):
        self.m1 = value


# Object Create
s1 = Student(34, 47, 32)
s2 = Student(89, 32, 12)

# Output
print(s1.add())
print(s2.add())
print(s1.avg_add())
print(s1.avg_add())
