entered_std =set()
rejected_std = set()

n = int (input("enter entry attemopt"))

for i in range(n):
    name = input("Enter student name")

    if name in entered_std:
        print(name,"Entry rejected .already entered")
        rejected_std.add(name)

    else:
        print(name,"Entry allowed")
        entered_std.add(name)
        

        