import pyfiglet
import sys
import random

from pyfiglet import Figlet
figlet = Figlet()

#for fonts
fonts_chosen = figlet.getFonts()
font_ = (random.choice(["3-d", "3x5", "5lineoblique", "acrobatic","lazy_jon", "krak_out", "roman"]))


if len(sys.argv) == 1 :
    str = input("Input: ")
    figlet.setFont(font=font_)
    print(figlet.renderText(str))
        
        
elif len(sys.argv)==3 and sys.argv[1]=="-f" or sys.argv[1]=="--font":
    if sys.argv[2] in fonts_chosen:
        str=input("Input: ")
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(str))
    else:
        sys.exit("Invalid font, please provide a valid font name")
    
else:
    sys.exit("Invalid usage")