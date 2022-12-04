#write a program to find the sum of digits of a given eber
e=eval(input("enter the no. :"))
s=0
rem=0
while e>0:
    rem=e%10
    e=e//10
    s=s+rem
print(s)

