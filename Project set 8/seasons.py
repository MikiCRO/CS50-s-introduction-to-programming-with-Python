from datetime import date, datetime, timedelta
import operator
import sys

import inflect

p=inflect.engine()

def main():
    birthdate  =get_birthdate (input("enter time in this format yyyy-mm-dd "))
    print_age_words(birthdate)
    
    
def get_birthdate(birthdate):
    try:
        today=date.today()
        time=datetime.strptime(birthdate, "%Y-%m-%d").date()
        new_time=operator.sub(today,time)
        print(new_time)
        return new_time

    except ValueError:
        print("Wrong format")
        sys.exit(1)
        
       

def print_age_words(birthdate):
    t=round(timedelta.total_seconds(birthdate)/60)
    words = p.number_to_words(t, andword="").capitalize()
    new_words=words+" minutes"
    print(new_words)
    
    
if __name__ == "__main__":
    main()
        