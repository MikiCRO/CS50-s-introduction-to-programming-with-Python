import random




while True:
    try:
        x=int(input("Level: "))
        if x>0:
            for m in range(0,x):
                m=range(0,x)
                p=random.choice(m)
                break
            while True:
                try:
                    y=int(input("Guess: "))
                    if y==p:
                        print("Just right")
                        break
                    elif y<p:
                        print("Too small")
                        continue
                    elif y>p:
                        print("Too big")
                        continue
                except ValueError:
                    continue
            break
    except ValueError:
        continue
    