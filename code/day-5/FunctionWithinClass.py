class Person:
    #self can be named anything, its like this in java
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age
    print("name is",name,"age is",age)

  def myfunc(abc,subject):
      abc.sub=subject
      print("subject is "+subject)

p1 = Person("Bhanu", 23)
p1.myfunc("computers")