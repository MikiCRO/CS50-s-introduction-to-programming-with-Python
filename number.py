def main():
    x=get_int("What is the x? ")
    print(f"X is {x}")



def get_int(prompt):
    while True:
        try:
            x=int(input(prompt))
            return x
        except ValueError:
            print("X is not an integer")
        

main()