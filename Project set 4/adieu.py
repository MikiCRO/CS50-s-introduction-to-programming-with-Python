
import inflect

def main():
    print(adieu())
    
def adieu():
    p=inflect.engine()
    names=[]

    while True:
        try:
            name=str(input("Name "))
            names.append(name)
        except EOFError:
            break
        
    names=p.join((names),final_sep=(","))
    return f"\nAdieu, adieu to {names}"


if __name__=="__main__":
    main()
        
