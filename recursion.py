n=int(input("Enter a no : "))
def fun(a):
    if (a==0 | a==1):
        return 1
    else:
        return a*fun(a-1)
print("The value of the factorial of",n,"is :",fun(n))  