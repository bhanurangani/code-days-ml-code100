
#this is how a function is created in pyhton
def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)
#function is called recursively
num = int(input("enter any number"))

#checking the number, because number less than 0 , its factorial cant be printed, and number if equal to 0 then its factorial is 1
#if number is more than 0 tha, its factorial is to be calculated by calling the function recursively
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of",num,"is",recur_factorial(num))