def greatestnumber(a,b,c):
    if a>=b and a>=c:
        if a==b:
            print("a is equal to b ")
        elif a==c:
            print("a is equal to c")
        else:
            
            print("greatest number is a",a)
    elif b>=a and b>=c:
        if b==a:
            print("b is equal to a ")
        elif b==c:
            print("b is equal to c")
        else:
            
            print("greatest number is b",b)
    elif c>=a and c>=b:
        if c==a:
            print("c is equal to a ")
        elif c==c:
            print("b is equal to c")
        else:
            print("greatest number is c ",c)
    else:
        
        print("invalid digit ")
        
