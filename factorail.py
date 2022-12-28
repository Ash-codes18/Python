# Program to find the factorail of a given number
a=1
b=int(input("Enter the no. for which you want to find the factorial: "))
for i in range(0,b+1):
    if i>1:
        a=a*i
print(a)
