#wap to find the factorial of a given no.
n=eval(input("enter the no. :"))
fact=1
result=1
while fact<=n:
    result=result*fact
    fact=fact+1
print(result)