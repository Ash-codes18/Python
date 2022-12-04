a = 1
b = 101
print("Prime number between",a,"and 100","are:")
for c in range(a,b):
    if c>1:
        for i in range(2,c):
            if (c%i)==0:
                break
        else:
            print(c)