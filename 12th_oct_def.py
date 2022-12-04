'''def sum(x,y):
    s=0;
    for i in range(x,y+1):
        s=s+i;
    print("sum of intergers: ", s)
sum(1,25)
sum(50,75)
sum(90,100)'''

'''def halua(x,y):
    h=0;
    for i in range(x,y+1):
        h=i
    print("This no. is greater among the two: ", h)
halua(435,5555)'''

d=[]
def sum(x,y):
    s=0

    for i in range(x,y+1):
        s=s+i
    print("sum of int:",s)
    d.append(s)
    d.sort()   
sum(1,25)
sum(50,75)
sum(45,56)
print("greater",d[-1])