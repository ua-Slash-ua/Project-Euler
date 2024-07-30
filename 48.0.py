l=[]
for i in range(1,1001):
    a  = (i**i)
    l.append(a)
a = str(sum(l))
print(a[-10:])