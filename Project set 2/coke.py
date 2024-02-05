c = [5,10,25]
coke=50
while True:
    x=int(input("INSERT COIN "))   #ask user for input
    
    while x not in c:            #if input not valid do the loop
        print("Amount Due: ",+coke)
        x=int(input("INSERT COIN "))
        
        if x not in c:
            continue
        elif x in c:             #once input is valid break
            break
    
    while x in c:                 #if and when input is valid do this
        ostatak=50 - x
        print("Ammount Due: ",+ostatak)
        
        while ostatak < 50:
            x=int(input("INSERT COIN "))
            if x not in c:
                print("Amount Due: ",+ostatak) 
                continue
            elif x in c:
            
                ostatak=ostatak-x
                if ostatak!=0 and ostatak>=1:
                    print("Amount Due: ",+ostatak) 
                    continue
                elif ostatak<=0:
                    print("Change owed: ",+abs(ostatak))
                    break
            
        break
    break
            


        
    
    
    
    