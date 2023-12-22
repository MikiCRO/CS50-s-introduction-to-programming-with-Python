while True:
    def main():
        while True:
            x=convert(input("Fraction: "))
            if x<=1:
                print("E")
                break
            elif x>=99 and x<=100:
                print("F")
                break
            elif x >100:
                continue
            else:
                print(f"{x}%")
                break
    def convert(x):
        y,z=x.split("/")
        y=int(y)
        x=float(y)/float(z)
        x=round(x,2)*100
        return x
    
    try:
        main()  
        break
    except ZeroDivisionError:
        print("", end="")
        continue
    except ValueError:
        print("", end="")
        continue

    




