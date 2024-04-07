n=int(input("Enter the length of the array(even): "))
if n%2==0:
    arr=[int(x) for x in input("Enter the array separated by',':").split(",")]
    mid=n/2
    mid_index=int(mid)
    Arr=[]
    for element in range(mid_index,n):
        Arr.append(arr[element])
    for i in range(0,mid_index):
        Arr.append(arr[i])
    print(Arr)
else:
    print("Enter Even Number!")
