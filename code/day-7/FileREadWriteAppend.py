#"r" - Read - Default value. Opens a file for reading, error if the file does not exist

#"a" - Append - Opens a file for appending, creates the file if it does not exist


#"w" - Write - Opens a file for writing, creates the file if it does not exist

#"x" - Create - Creates the specified file, returns an error if the file exists
#file is being opened, but it will not do anything because file isnt present
f=open("Hello.txt","rt")
print(f.read())
f.close()

#actually now the file is created,
c=open("Hello.txt","a")
c.write("and i have appended this intp the file")

c.close()
c=open("Hello.txt","rt")
print(c.read())

c.close()

