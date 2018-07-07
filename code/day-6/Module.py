#a file with name module.py is created which is to be inherited/imported in the other file
class personal:
    #a function namely personal is created
    def per(name,age):
        n=name
        n=str(n)
        a=age
        a=int(a)
        print("the age is",a)
        print("the name is",n)

#object p1 is created
p1=personal
#function is called using the object
p1.per("bhanu",23)