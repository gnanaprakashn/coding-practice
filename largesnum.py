def largesnum(a):
    largest = a[0] # we assume that first value is largest 
    for i in range(len(a)):
        if a[i]>largest:
            #its only get change if i is greater than largest variable
            largest = a[i]

    print(largest)

            
            
largesnum([3,4,10,5,7])
