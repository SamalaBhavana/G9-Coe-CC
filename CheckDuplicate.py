#Check Duplicate
arr=[int(x) for x in input("Enter the Array Elemnts separated by ',': ").split(',')]
n=len(arr)
has_Dup=False
for i in range(n):
    for j in range(i+1,n):
        if arr[i]==arr[j]:
            has_Dup=True
            #break
   # if has_Dup:
       # break
if has_Dup:      
    print("Has Duplicate elements")
else:
     print("No duplicate element")
