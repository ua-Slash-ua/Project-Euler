a=100
b=100
l=[]
def pol(s):
    if str(s) == str(s)[::-1]:
        l.append(s)
while a<=999:
    s=a*b
    pol(s)
    for b in range(100,1000):
        s=a*b
        pol(s)
    a+=1
print(max(l))