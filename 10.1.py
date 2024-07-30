n=2000000
num=list(range(2,n+1))
for i in num:
    if i!=0:
        for k in range(2*i,n+1,i):
            num[k-2]=0
print(sum(list(filter(lambda x:x!=0,num))))