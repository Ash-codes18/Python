'''
a=int(input())
d="* "*(a)
c=len(d)
c=c-3
e="#"*c
print(d)
for i in range(a-2):
    print("*","*",sep=e)
print(d)
print()
print("*")'''

a=int(input("rows: "))
print()
for i in range(a):
    for k in range(a):
        print("*",end=" ")
    print()

print()
print()


print("For empty square :",a)
print()
for p in range(a):
    if p==0 or p==(a-1):
        for q in range(a):
            print("*",end=" ")
        print()
    else:
        for f in range(a):
            if f==0 or f==a-1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

print()
print()

print("For diagonals square:",a)
print()
for p in range(a):
    if p==0 or p==(a-1):
        for q in range(a):
            print("*",end=" ")
        print()
    else:
        for f in range(a):
            if f==p or f==a-p-1:
                print("*",end=" ")
            elif f==0 or f==(a-1):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

print()
print()

print("For diagonals square empty:",a)
print()
for p in range(a):
    if p==0 or p==(a-1):
        for q in range(a):
            print("*",end=" ")
        print()
    else:
        for f in range(a):
            if f==p:
                print(" ",end=" ")
            elif f==0 or f==(a-1):
                print("*",end=" ")
            else:
                print("*",end=" ")
        print()

print()

print("For diagonals square empty:",a)
print()
for p in range(a):
    if p==0 or p==(a-1):
        for q in range(a):
            print("*",end=" ")
        print()
    else:
        for f in range(a):
            if f==a-p-1:
                print(" ",end=" ")
            elif f==0 or f==(a-1):
                print("*",end=" ")
            else:
                print("*",end=" ")
        print()

print()
print()

print("For diagonals square:",a)
print()
for p in range(a):
    if p==0 or p==(a-1):
        for q in range(a):
            print("*",end=" ")
        print()
    else:
        for f in range(a):
            if f==p or f==a-p-1:
                print(" ",end=" ")
            elif f==0 or f==(a-1):
                print("*",end=" ")
            else:
                print("*",end=" ")
        print()

print()
print()
for i in range(a):
    for j in range(a):
        if i==0 or i==a-1:
            print("*",end=" ")
        else:
            if j==0 or j==a-1 or j==a//2 or i==a//2:
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()