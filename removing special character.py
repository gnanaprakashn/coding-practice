#removing the special character without using regular expression
def a(b):
    cleaned = ""
    for i in b:
        if i.isalnum() or i.isspace():
            #if the i is only alphabet,space and number then add into that variable  else not
            cleaned+=i
        
    print(cleaned)

a("example&& usecase")
