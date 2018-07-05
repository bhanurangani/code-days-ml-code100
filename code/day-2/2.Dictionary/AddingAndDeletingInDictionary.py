thisdict={
    "ayush":"comedian",
    "bhanu":"poet",
    "yuvraj":"youtuber",
    "suyash":"lazy"
}
print(thisdict)
#adding the element
thisdict["aman"]="not a partner"

print(thisdict)

#removing any element

del(thisdict["aman"])

print(thisdict)

#the expected output
#{'ayush': 'comedian', 'bhanu': 'poet', 'yuvraj': 'youtuber', 'suyash': 'lazy'}
#{'ayush': 'comedian', 'bhanu': 'poet', 'yuvraj': 'youtuber', 'suyash': 'lazy', 'aman': 'not a partner'}
#{'ayush': 'comedian', 'bhanu': 'poet', 'yuvraj': 'youtuber', 'suyash': 'lazy'}

