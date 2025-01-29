""" . write a program that performs both addition and subtraction with them. However, if any subtraction results in a negative 
number, display it as a positive value. How will you tackle this and show the final 
results?"""
def absnumber(a,b):
    print(f'addition of {a}+{b} =',abs(a+b))#using absolute function we can get the postive number at last
    print(f'Subtraction of {a}+{b} =',abs(a-b))

absnumber(20,-150)
