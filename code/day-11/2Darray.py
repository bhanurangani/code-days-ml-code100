from array import *
n=int(input("enter the number of columns"))
m=int(input("enter the number of rows"))
arr=[[0 for i in range(n)] for j in range(m)]

for i in range(0,m):
    for j in range(0,n):
       arr[i][j]=input("enter")

for i in range(0,m):
    for j in range(0,n):
        print(arr[i][j],end=" ")
    print("")
