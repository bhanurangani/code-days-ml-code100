import os
if(os.path.exists("user.txt")):
    os.remove("user.txt")
    print("file removed")
else:
    print("file not found")
