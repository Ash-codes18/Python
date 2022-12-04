def halua(x):
    c=0
    for i in x:
        c=c+i
        return c
x=int(input())
y=int(input())
z=int(input())
l=[x,y,z]
b=[]
c=[]
dd=[]
for b in l:
    for c in l:
        for d in l:
            cc=[b,c,d]
            dd.append(cc)
dd.sort(key=halua)
print(dd)


    #b.append(x)
     #   c.append(y)
      #      d.append(z)
        #    if (x+y+z!=3):
# print(list)