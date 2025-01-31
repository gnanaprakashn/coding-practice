def palindromechecker(a):
    b="".join(i for i in a.lower() if i.isalnum())
    print(b)
    print(b==b[::-1])

  

