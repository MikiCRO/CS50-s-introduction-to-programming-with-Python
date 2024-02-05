from validator_collection import validators,checkers, errors

 
try:    
    emails = validators.email(input("Enter your Email "))
    is_email = checkers.is_email(emails)
    print("Valid")

except errors.InvalidEmailError:
    print("Invalid")
        

           