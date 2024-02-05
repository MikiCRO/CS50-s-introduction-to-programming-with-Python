x=input("Input: ").translate({ord(ch):'' for ch in 'aeiou'}) 

print("Output: " + x)

#or 
#   string = input("Input: ")
#   vowels = "aeiouAEIOU"
#
#   for i in vowels:
#       string = string.replace(i, "")

#   print(string)