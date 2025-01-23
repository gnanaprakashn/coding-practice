#2.Age Group Classification:
'''0-12: Child
13-19: Teenager
20-64: Adult
65 and above: Senior'''

def AgeGroupClassification(age):
    if age<=0:
        print("wrong input")
    elif age>0 and age<=12:
        print("child")

    elif age>12 and age<=19:
        print("Teenager")
        
    elif age>20 and age<=64:
        
        print("Adult")
    else:
        print("Senior")
