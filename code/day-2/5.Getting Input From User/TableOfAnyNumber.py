#table printing of any number
i=1
#getting input from user using input function
x=input("enter any number to print its table")
#type casting
x=int(x)
while i <= 10 :
    print(x,"X",i,"=",x*i)
    i += 1
