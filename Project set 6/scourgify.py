import csv, sys


if len (sys.argv) <3 :
    print("To few command line arguments")
    sys.exit()
elif len (sys.argv) >3 :
    print("To many command line arguments")
    sys.exit()
    
else:
    if sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
        try:
            with open (sys.argv[1],mode="r") as csvfile:
                reader = csv.DictReader(csvfile)
                    
                with open(sys.argv[2],"w",newline="") as csvfile:
                    fieldnames=["last", "first", "house"]   
                    writer=csv.DictWriter(csvfile,fieldnames=fieldnames)  
                    writer.writeheader()
                    for row in reader:
                        last,first=row["name"].split(",")
                        house=row["house"]
                        writer.writerow({"last":last.strip(),"first":first.strip(),"house":house})
                    
        except FileNotFoundError:
            print("File not found")
            sys.exit()    
    else:
        print("Not a csv File")
        sys.exit()
