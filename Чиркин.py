a= int(input ("Please enter the Total Number of List Elements:"))
b=[]
for i in range (a):
    i+=1
    c=int(input("Please enter the Value of  (0) Element:".format(i)))
    if (c % 2 ==0):
        b.append (c)
print (b)
