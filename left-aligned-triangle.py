# Print a left-aligned triangle
def lefttriangle(a):
    for i in range(1,a+1):
        #print the space then *, space will drop one by one , star get multiple one by one
        print(" "*(a-i)+"*"*i)
        
lefttriangle(5)
