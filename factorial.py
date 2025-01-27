def factorial(a):
    if a == 1:
        return 1
    elif a > 1:
        #it gets recursive  like for 3 . it gives 3 2 1 
        return a * factorial(a - 1)
    else:
        return 0

print(factorial(3))  

