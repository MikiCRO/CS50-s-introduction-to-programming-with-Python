from tabulate import tabulate
import sys
import csv

if len (sys.argv) <2 :
    print("To few command line arguments")
    sys.exit()
elif len (sys.argv) >2 :
    print("To many command line arguments")
    sys.exit()
    
else:
    if sys.argv[1].endswith(".csv"):
        try:
            with open (sys.argv[1],mode="r") as csvfile:
                csvFile = csv.reader(csvfile)
                print(tabulate(csvFile,headers="firstrow",tablefmt="grid"))
                
        except FileNotFoundError:
            print("File not found")
            sys.exit()    
            
    else:
        print("Not a csv File")
        sys.exit()
            
            
            
            
