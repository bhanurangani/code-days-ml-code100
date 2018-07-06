#class is defined
class personal:
    #__init__() is a function All classes have a function called __init__(), which is always executed when the class is being initiated.

    #Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
    def __init__(self,name,age,gender):
        self.n=name
        self.a=age
        self.g=gender

x=str(input("enter the name of the person"))
y=int(input("enter the age"))
z=str(input("enter the gender"))

#putting parameters in class
p1=personal(x,y,z)

print("the name is",p1.n,"of age",p1.a,"and gender",p1.g)