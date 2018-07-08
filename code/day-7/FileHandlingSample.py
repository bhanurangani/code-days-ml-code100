#opening the file
#"r" - Read - Default value. Opens a file for reading, error if the file does not exist

#"a" - Append - Opens a file for appending, creates the file if it does not exist


#"w" - Write - Opens a file for writing, creates the file if it does not exist

#"x" - Create - Creates the specified file, returns an error if the file exists
f=open("simple.txt")
#fiel is being read and printed
print(f.read())
f.close()

we=open("simple.txt","w")
we.write("i wish i was a billionair")
we.close()
re=open("simple.txt","rt")
print(re.read())
re.close()