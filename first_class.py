E=int(input(" enter the marks obtained in english :"))
M=int(input("enter the marks obtained in maths :"))
C=int(input("enter the marks obtained in chemistry :"))
P=int(input ("enter the marks obtained in physics :"))
CS=int(input("enter the marks obtained in computer science"))
PHE=int(input("enter the marks obtained in physical education"))
Total=E+M+P+CS+PHE+C
print(Total)
p= Total/600 * 100
print(p)
if p>=90:
    print("grade=A")
elif p<90 and p>80:
    print("grade=B")
elif p<80 and p>70:
    print("grade=C")
elif p<70 and p>60:
    print("grade=D")
else:
    print("FAIL")

