'''m = int(input("Enter the number: "))
for i in range(1,11,2):
    print(m,"*",i, "=", m*i)'''

'''n=int(input("Enter the no. :"))
for i in range(n):
    for j in range(n,i):
        print("*",end=" ")
    print("")'''
 
n=eval(input("Enter the no.:"))
for i in range(n):
    for j in range(n,i):
        for k in range(i,j):
            print("*",end="")
        print("")
        #get the half diamond pattern printed
