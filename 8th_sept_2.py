s=0
d=0
for i in range(1,31,2):
    if i%2==0 or i%5==0:
        s=s+i
    else:
        d=d+i
print(d-s)
        