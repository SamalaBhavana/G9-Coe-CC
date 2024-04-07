#display Duplicate
arr=[int(x) for x in input("Enter the array elements separated by ',': ").split(",")]
n=len(arr)
Dup=[]
for i in range(n):
    for j in range(i+1,n):
        if arr[i]==arr[j] and arr[i] not in Dup:
            Dup.append(arr[i])
print(Dup)
