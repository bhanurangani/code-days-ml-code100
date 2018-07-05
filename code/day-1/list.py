#this is how list is created
#list is like array
thislist=["ayush","bhanu","suyash","yuvraj"]

print(thislist)

#some basic function on list

#append: to add an element in list
thislist.append("no-one else")

print(thislist)

#modifing element
thislist[0]="saxena"

print(thislist)

#removing any element while printing, it doesn't make any change in the original file of the list
thislist.remove(thislist[4])

print(thislist)

#printing the length of the list
print(len(thislist))

#coping the list into another list, using a function
x=thislist.copy()

print(x)

#reversing the list into its original set
thislist.reverse()

print(thislist)

#sorting the list at printing level
print(sorted(thislist))

#sorting the lkist, in the original set
thislist.sort()

#deleting any emenet from the list
thislist.pop(2)

print(thislist)

print(thislist[2])

#inserting any element in the list at any index, the elmenent present on that index will be shifted ahead
thislist.insert(2,"suyash")

print(thislist)

#returning the index of any element
y=thislist.index("saxena")
print(y)


z=["project","partners"]
thislist.extend(z)

print(thislist)

thislist.clear()

print(thislist)