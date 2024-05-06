import csv
import re
from collections import Counter


grocery=[]
try:
    while True:
        with open("grocery.txt", "a") as file:
            grocer=input().upper()
            file.write(grocer + "\n")
            file.close
            continue
except EOFError:
    
    with open("grocery.txt", "r") as file:
        grocery=file.readlines()
        
        for line in sorted(set(grocery)):   #set is used if we input milk 2 times,it cant cointain two items(duplicates)
            count=grocery.count(line)     #counting lines
            if count>1:
                print(f"{count} {line}", end="")
            elif count==1 :
                print(f"1 {line}", end="")

        with open("grocery.txt", "w") as file:
            file.truncate(0)
        
