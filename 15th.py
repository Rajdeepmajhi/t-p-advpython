var2 = set()
var1 = set()
n = int(input("Enter no of student : "))
for i in range (n):
    name = input("Enter your name : ")
    if name in var1 :
        print ("Name is alredy exists.")
    else:
        var1.add(name)
    print(var1)
