def fibinoseries(n):
    a=-1 #fibinoseries starts with zero and ones
    b=1
    for i in range(n):
        #it just swap and add the numbers
        a,b=b,a+b
        print(b)
    

fibinoseries(10)
