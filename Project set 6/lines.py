import sys

count=0

if len (sys.argv) <2 :
    print("To few command line arguments")
    sys.exit()
elif len (sys.argv) >2 :
    print("To many command line arguments")
    sys.exit()
  
else:
    if sys.argv[1].endswith(".py"):
        try:
            with open (sys.argv[1],"r") as file:
                sys.argv[1].lstrip()
                for line in file:
                    if line.isspace():
                        continue
                    else:
                        if line.startswith("#"):
                            
                            continue
                        else:
                            count+=1
                print(count)
        except FileNotFoundError:
            print("File not found")
            sys.exit()
    else:
        print("Not a python file")
        sys.exit()
    
