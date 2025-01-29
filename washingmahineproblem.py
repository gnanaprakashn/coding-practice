def washingmahineproblem(value,size):
    a = value
    b = size.lower()
    if a==0:
        print("time Estimated :0 minutes")
    elif b == "l" and a<=2000:
        print("Timr Estimated : 25 Minutes")
    elif b == "m" and (a>2000 and a<=4000):
        print("Timr Estimated : 35 Minutes")
        
    elif b == "h" and (a>4000 and a<=7000):
        print("Timr Estimated : 45 Minutes")
    elif  b == "h" and  a>7000:
        print("Weight Overloaded")
    else:
        print("Invalid Input")

washingmahineproblem(4001,"h")
