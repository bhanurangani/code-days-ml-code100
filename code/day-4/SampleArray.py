#below is the emplty arrya list
partenrs=[]
#now taking input from user
n=int(input("enter thr number of partners in the project"))

for k in range(n):
    #remember that insert function is to be used, where the 1st parameter is the index, and second is the object
    partenrs.insert(k,input("enter the name"))


print("partners are")
for j in range(n):
    #here j is the index
    print(partenrs[j])