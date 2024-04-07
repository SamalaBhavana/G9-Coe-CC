#First Even Next Odd
arr=[int(x) for x in input("Enter Array separated by',': ").split(",")]
Res=[]
for i in arr:
    if i%2==0:
        Res.append(i)
for i in arr:
    if i%2!=0:
        Res.append(i)
print(Res)
