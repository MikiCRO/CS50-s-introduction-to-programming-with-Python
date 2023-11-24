try:
    math=input("Expresion: ")


    x, y, z=math.split(" ")
    x=int(x)
    z=int(z)


    if y == "+":
        result = round(x+z,1)
        print(f"{result:.1f}")
            
    elif y == "-":
        result = round(x-z,1)
        print(f"{result:.1f}")
            
    elif y == "*":
        result = round(x*z,1)
        print(f"{result:.1f}")
            
    elif y == "/":
        result = round(x/z,1)
        print(f"{result:.1f}")
except ValueError:
    print("Use just one indent between characters")
    

    
