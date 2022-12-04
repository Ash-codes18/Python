#WAP to get the sum of the nos. from 1 to 20 that are not divisible by 2,3 or 5
s=0
for i in range(1,20):
    if i%2==0 or i%3==0 or i%5==0:
        continue
    else:
        s=s+i
        print(s)