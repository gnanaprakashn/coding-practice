def hallowsquare(r,c):
    for i in range(1,r+1):
        if i ==1 or i ==r:
            #only 1 and last row print the whole star
            print("*"*c)
        else:
            #other print the first and lasr value of the star inbetween it print rhe space
            print("*"+" "*(c-2)+"*")

hallowsquare(4,4)
