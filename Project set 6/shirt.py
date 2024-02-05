import sys
from PIL import Image
import PIL
from PIL import ImageOps
import os

suffixes=(".jpg",".png")

if len (sys.argv) <3 :
    print("To few command line arguments")
    sys.exit()
elif len (sys.argv) >3 :
    print("To many command line arguments")
    sys.exit()
else:
    input_ext = os.path.splitext(sys.argv[1])[1].lower()
    output_ext = os.path.splitext(sys.argv[2])[1].lower()

    if sys.argv[1].endswith(suffixes)  and sys.argv[2].endswith(suffixes):
        try:
            shirt=Image.open("shirt.png")
            size=shirt.size
            muppet=Image.open(sys.argv[1])
            muppet=PIL.ImageOps.fit(muppet,size)
            muppet.paste(shirt,shirt)
            muppet.save(sys.argv[2])
            
        except FileNotFoundError:
            print("File not found")
            sys.exit()
    else:
        print("Not a jbg or png file")
        sys.exit()
    
    