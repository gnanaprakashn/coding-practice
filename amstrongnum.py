def amstrongnum(a):
    b =0
    p = len(str(a)) #get the len of the number for power
    for i in str(a):# convert this to str to get induvidual number
        b +=int(i)**p #power the individual number and all all this number
    if b==a:
        print("this is amstrongnum")
    else:
        print("this is not a amstrongnum")


amstrongnum(153)
        
