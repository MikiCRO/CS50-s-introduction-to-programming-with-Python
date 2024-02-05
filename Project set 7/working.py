import re
import sys


def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
    if matches:=re.search(r"^(\d+):?(\d+)? (AM|PM) (to) (\d+):?(\d+)? (AM|PM)$",s,re.IGNORECASE):
        if "AM" in matches.group(3) and "PM" in matches.group(7):
            if matches.group(1)=="12" and matches.group(5)=="12":
                return("00:00 to 12:00")
            else:
            
                n=matches.group(1)
                n=int(n)
                n=("%02d"%n)
                
                i=matches.group(5)
                i=int(i)
                i=i+12
                i=str(i)
                if matches.group(2)==None and matches.group(6)==None:
                    return(n+":00"+" "+matches.group(4)+" "+i+":00")
                else:
                    
                    if int(matches.group(2))>=60 or int(matches.group(6))>=60:
                        raise ValueError
                    else:
                        return(n+":"+matches.group(2)+" "+matches.group(4)+" "+i+":"+matches.group(6))
            
        elif "PM" in matches.group(3) and "AM" in matches.group(7):
            n=matches.group(5)
            n=int(n)
            n=("%02d"%n)
            
            i=matches.group(1)
            i=int(i)
            i=i+12
            i=str(i)
            if matches.group(2)==None and matches.group(6)==None:
                return(i+":00"+" "+matches.group(4)+" "+n+":00")
            else:
                if int(matches.group(2))>=60 or int(matches.group(6))>=60:
                    raise ValueError
                else:    
                    return(i+":"+matches.group(2)+" "+matches.group(4)+" "+n+":"+matches.group(6))
    else:
        raise ValueError        
if __name__ == "__main__":
    main()