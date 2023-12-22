
import datetime


month= {
    "January" :1,
    "February":2,
    "March":3,
    "April":4,
    "May":5,
    "June":6,
    "July":7,
    "August":8,
    "September":9,
    "October":10,
    "November":11,
    "December":12
}

while True:
    try:
        x=input("date ")
        dt = datetime.datetime.strptime(f"{x}", "%m/%d/%Y")
        print ('{0}-{1:02}-{2:02}'.format(dt.year, dt.month, dt.day % 100))
        break
        
    except ValueError:
        try:
            mjesec,dan,godina=x.split(" ")
            mjesec=str(mjesec)
            dan=str(dan)
            godina=str(godina)
            if mjesec in month:
                mjesec = month[mjesec]
                mjesec=str(mjesec)
                mjesec=mjesec+" "+dan+" "+godina
                dt = datetime.datetime.strptime(f"{mjesec}", "%m %d, %Y")
                print ('{0}-{1:02}-{2:02}'.format(dt.year, dt.month, dt.day % 100))
                break
            else:
                continue
        except ValueError:
            continue     
            
       
        