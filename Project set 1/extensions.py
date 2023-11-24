x=input("File name: ").strip().lower()

if x.endswith(".jpeg"):
    print("image/jpeg")
    
elif x.endswith(".jpg"):
    print("image/jpg")
    
elif x.endswith(".gif"):
    print("image/gif")
    
elif x.endswith(".png"):
    print("image/png")
    
elif x.endswith(".pdf"):
    print("application/pdf")
    
elif x.endswith(".txt"):
    print("document/txt")
    
elif x.endswith(".zip"):
    print("file/zip")
    
else:
    print("application/octet-stream")