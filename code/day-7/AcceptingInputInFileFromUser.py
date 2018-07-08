#open() function is used to open the file
#"r" - Read - Default value. Opens a file for reading, error if the file does not exist

#"a" - Append - Opens a file for appending, creates the file if it does not exist


#"w" - Write - Opens a file for writing, creates the file if it does not exist

#"x" - Create - Creates the specified file, returns an error if the file exists
f=open("user.txt","w")
#write() function is used to write text inside file
f.write(input("enter what you wish to enter  in the file"))
#fiel is closed
f.close()
#now opening file to be read
c=open("user.txt","rt")
#printing whats present in the file
print(c.read())

c.close()