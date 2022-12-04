# d1=int(input())
# d2=int(input())
# dict3=[d1[i]:d2[i] for i in range(len(d2))]
# print(dict3)


x=int(input())
y=int(input())
z=int(input())
print(list([b,c,d] for b in range(x+1) for c in range(y+1) for d in range(z+1) if (x+y+z!=3)))  