def findingdivisor(a):
    b= []
    c=0
    for i in range(1,a):
        if a%i==0:
            b.append(i)
            c+=i
    print(b)
    print(c)
    print(a==c)
