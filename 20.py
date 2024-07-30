a =100
f =1
s= 0
for i in range(1,a+1):
    f*=i
f =str(f)

for e in range(0,len(f)):
    s+=int(f[e])
print(s)