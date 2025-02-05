def perfectnumbe(num):
    a = 0
    for i in range(1,(num//2)):
        
        if num%i==0:
            
            a+=i
            
            print(a)

    if a==num:
        print("this is perfect number")
    else:
        print("this is not a perfect number")
        
            
