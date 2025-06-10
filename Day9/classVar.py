# instance variable = all objects has their own attribute
# class variable is shared among all objects(instances of a class)

class Student:
    class_year = 2025 # can be accessed using name of the class
    num_students = 0
    all_students = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1
        Student.all_students.append(self)

student1 = Student("Pragyan", 21)
student2 = Student("Someone",20)
student3 = Student("Fang Yuan",22)

# print(student2.name)
# print(student2.age)
# print(student1.class_year)

# print(Student.class_year)
# print(Student.num_students)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students.")
# print(Student.all_students)
for student in Student.all_students:
    print(student.name)