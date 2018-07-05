a=22
b=11
c=4
# using nested if condition
if a>b :
    if a>c :
        print("a is greatest")
    elif a<c :
        print("c is greatest")

    else:
        print("a and c are equal")

if b>a :
    if b>c :
        print("b is greatest")
    elif c>b :
        print("c is greatest")

    else :
        print("b and a are equal")

