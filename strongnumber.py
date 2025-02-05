def strongnumber(num):
    a = str(num)
    c=1
    cc =0
    for i in a:
        print(i)
        c=1
        
        for j in range(1,int(i)+1):
            c*=j
        cc+=c
        print(cc)
        
    if cc==num:
        print("this is stron  number")
    else:
        print("this is not a strong number")



