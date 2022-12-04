'''for i in range(1,100,1):
    if i==11:
        break
    else:
        print(i)'''

num=int(input())
x=num
for i in range(2,num):
    if (num%i==0):
        flag=0
        break
    else:
        flag=1
    if (flag==1):
        print("prime")
    else:
        print("not prime")
