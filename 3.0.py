s = 600851475143
a = 3
l=[]
while True:
    o=[]
    a+=1
    if s<=1:
        break
    elif s%a==0:
        for i in range(1,a+1):
            if a%i==0:
                o.append(i)
        if len(o)==2:
            l.append(a)
            s/=a
print(max(l))