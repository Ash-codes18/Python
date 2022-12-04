# class college:
#      def __init__(course,name,roll):
#           course.name = name #("halua")
#           course.roll = roll #("66")
# a= college("halua","66")
# print(a.name)
# print(a.roll)

'''class college:
     def __init__(self,f1,f2):
          self.f1 = f1
          self.f2 = f2
     def __str__(self):
          return f"{self.f1}{self.f2}"
p=college("yash","55")
print(p)'''
'''class college:
     def __init__(self,f1,f2,f3,f4,f5,f6):
          self.f1 = f1
          self.f2 = f2
          self.f3 = f3
          self.f4 = f4
          self.f5 = f5
          self.f6 = f6
     def add(self):
          print("My name is "+self.f1,"My age is "+self.f2, sep="\n")
          print("My name is "+self.f3,"My age is "+self.f4, sep="\n")
          print("My name is "+self.f5,"My age is "+self.f6, sep="\n")
p=college("Heena","28","meena","27","deeka","27")
p.add()'''

'''class college:
     def __str__(self,f1,f2):
          return f"{self.f1}{self.f2}"
a=college("ash","99")
print(a.f1)
print(a.f2)'''

# class college:
#      def __init__(self,f1,f2):
#           self.f1 = f1
#           self.f2 = f2
#           def __str__(self):
#                return f"{self.f1}{self.f2}"
# p=college("yash","55")
# del p.f1
# print(p)

class college:
     def __init__(self,f1,f2):
          self.f1 = f1
          self.f2 = f2
     def __str__(self):
          return f"{self.f1}{self.f2}"
p=college("yash","55")
print(p)
del p.f1
print(p.f2)
