a = 2000000
lt=[]
for u in range(1,a+1):
    l=[]
    for i in range(1,u+1):
        if u%i==0:
             l.append(i)
        if len(l) > 2:
            continue
    if len(l)==2:
        lt.append(u)
    print('a=', u)
print(sum(lt))