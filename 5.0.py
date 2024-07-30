a=10
while True:
    f=0
    for i in range(1,21):
        if a%i==0:
            f+=1
    if f==20:
        print('a=',a)
        break
    a+=10