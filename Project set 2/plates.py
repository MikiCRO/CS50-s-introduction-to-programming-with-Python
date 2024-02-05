def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if rule1(s)==True and rule2(s)==True and rule3(s)==True:
        return True
    else:
        return False
    
def rule1(t):
    if len(t) >= 2 and len(t) <= 6:
        if t.isalnum():
            return True
            
    else:
        return False
    
def rule2(k):
    if k[0].isdigit() or k[1].isdigit():
        return False
    else:
        return True
    
def rule3(p):
    for i,v in enumerate(p):
        if v.isdigit():
            if v=="0":
                return False
            elif any(p[i+1].isalpha() for i in range(i,len(p)-1)):
                return False
            else:
                return True
        elif all(p.isalpha() for i in p):
            return True
        
main()