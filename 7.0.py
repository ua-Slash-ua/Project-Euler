a=1
l=[]
n=10001
while True:
    lt=[]
    for i in range(1,a+1):
        if a%i==0:
            lt.append(i)
    if len(lt)==2:
        l.append(a)
        print(len(l))
    if len(l)==n:
        break
    a+=1
print(l[n-1])