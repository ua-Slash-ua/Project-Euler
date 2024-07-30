n=1
l={}
def pro(a):
    s=1
    while True:
        if a%2==0:
            a=a/2
            s+=1
        elif a==1:
            break
        else:
            a=a*3+1
            s+=1
    l[n]=s

while True:
    if n == 1000000:
        break
    pro(n)
    n+=1
maxi=max(l, key = l.get)
print('max_step=',l[maxi])
print('number=',maxi)