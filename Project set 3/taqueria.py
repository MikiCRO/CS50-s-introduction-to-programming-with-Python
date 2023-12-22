order= {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }

price=0

while True:
    try:
        d=input("G  ")

        if d in order:
            price=order[d] + price
            print(f"Total price {price}$")
    except EOFError:
        print("", end="")
        break   
            
            

        
    

        
        
        
            
        
      