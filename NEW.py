# class Student:
#     def __init__ (self,name,age,email):
#         self.name=name
#         self.age=age
#         self.email=email
# Stud_1 = Student('Sri ram',25,'ram@sch.com')
# Stud_2 = Student('raghu ram',28,'lak@sch.com')
# print('s1d =', Stud_1.name, Stud_1.age, Stud_1.email)
# print('s2d =', Stud_2.name, Stud_2.age, Stud_2.email)

class Student:
    pass
Stud_1 = Student()
Stud_2 = Student()
name=input("name: ")
age=int(input("age: "))
email=input("email:")
name1=input("name 1: ")
age1=int(input("age 1: "))
email1=input("email 1:")
Stud_1.name = name
Stud_1.age=age
Stud_1.email=email
Stud_2.name1 = name1
Stud_2.age1=age1
Stud_2.email1=email1
print("Stud_1.name:", Stud_1.name)
print("Stud_1.age:", Stud_1.age)
print("Stud_1.email:", Stud_1.email)
print("Stud_2.name:", Stud_2.name1)
print("Stud_2.age:", Stud_2.age1)
print("Stud_2.email:", Stud_2.email1)


