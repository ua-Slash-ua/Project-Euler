def pro(num):
    s=0
    sq=int(num**0.5)
    for i in range(1,sq+1):
        if num%i==0:
            s+=2
    if sq**2==num:
        s-=1
    return s
def tri(dil):
    n=1
    while True:
        num=n*(n+1)//2
        ln=pro(num)
        if ln>dil:
            return num
        n+=1
res=tri(500)
print(res)



