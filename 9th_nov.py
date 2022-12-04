#print the vowels
#change the case of the letters
#eliminate character that is given input by the user
'''a=input("Enter the value for which the case is to be changed : ")
print(a.swapcase()) 
c=["a","e","i","o","u","A","E","I","O","U"]
for vowel in a:
    i=[]
    if vowel in c:
        i=i.append(vowel)
        print( vowel) 
        print(i)
d=input("Enter the letter to be replaced : ")
x=input("Enter the letter that will replace the given letter : ")
e=a.replace(d,x,1)
print(e)'''
'''l1=["Raamu,Shaamu","18,20","kela,seb","car,train"]
l2=["seeta,geeta","16,18","gajar,mooli","cycle,scooty"]
print(l1+l2)
print(l1 in l2)
print((l1,l2)*3)
print(l1 is l2)
del l1[1]
print(l1)'''

    b=[]
    a=int(input("enter the no. of list items : "))
    for i in range(0,a):
        m=int(input())
        b.append(m)
print("list given input by user:",b)
l1=[]
l2=[]
for i in b:
    if i%2==0:
        l1.append(i)
    else:
        l2.append(i)
print("even elements in the list:",l1)
print("odd elements in the list:",l2)





























'''a=[]
b=int(input("Enter the no. of elements : "))
for i in range(0,b):
    f=int(input())
    a.append(f)
print(a)'''





