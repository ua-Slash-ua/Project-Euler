a = 1
b = 2
c = 4000000
l = []
while True:
    if a%2==0:
        l.append(a)
    if b%2==0:
        l.append(b)
    a+=b
    b+=a
    if a>=c or b>=c:
        break
print(sum(l))
