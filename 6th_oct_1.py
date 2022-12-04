T=(int(input("enter range: ")))
a=input("enter your string with space: ")
b=input("enter your string without space: ")
for i in range(T):
    if i==5:
        print(b)
        continue
    else:
        print(a)