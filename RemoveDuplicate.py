#Remove Duplicates
arr=[int(x) for x in input("Enter the array elements separated by ',': ").split(",")]
n=len(arr)
Arr=[]
yes=False
for element in arr:
    if element not in Arr:
        Arr.append(element)
print(Arr)
