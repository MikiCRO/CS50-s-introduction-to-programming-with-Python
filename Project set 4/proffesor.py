import random

def main():
    level = get_level()

    score = 0
    attempts = 0
    wrong_answer=0
    
    while True:
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y
        
        while True:
            try:
                user_answer = int(input(f"{x} + {y} = ")) 
                if answer==user_answer:
                    score=score+1
                    attempts=attempts+1
                    break
                elif answer!=user_answer:
                    score=score
                    attempts=attempts
                    wrong_answer=wrong_answer +1
                    
                    print("EEE")
                    if wrong_answer==3:
                        wrong_answer=0
                        attempts=attempts+1
                        print("EEE")
                        print(f"{x} + {y} = {answer} ")
                        break
                    
                    
                
                        
                    continue
            except ValueError:
                print("EEE")
                break
                
        if attempts==10:
            print(score)
            break
            
        else:
            continue
         
                
        
               
    
    
    
  

def get_level():
  while True:
    try:
      level = int(input("Level: "))

      if level < 1 or level > 3:
        raise ValueError
      else:
        return level
    except ValueError:
      pass
        
def generate_integer(level):
    if level == 1:
        n = random.randint(0, 9)
    elif level == 2:
        n = random.randint(0, 15)
    elif level == 3:
        n = random.randint(7, 25)   
    return n
    

    



main()