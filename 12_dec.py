# class Employee:
#     pass
# Emp1=Employee()
# a=input("Enter the name of the Employee: ")
# Emp1.name=a
# Emp1.age=25
# Emp1.salary=25000
# print('Emp1.name:',Emp1.name)
# print('Emp1.salary:',Emp1.salary)

class Car:
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
Honda=Car()
name=input("car name: ")
Honda.setName(name)
print("Honda car name: ", Honda.getName())