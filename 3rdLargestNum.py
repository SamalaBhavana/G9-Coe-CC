#Find 3rd largest Number
arr=[int(x) for x in input("Enter Array separated by',': ").split(",")]
n=len(arr)
if n>=3:
    max1=arr[0]
    max2=arr[1]
    max3=arr[2]
    for num in arr:
        if num > max1:
            max3=max2
            max2=max1
            max1=num
        elif max2<num<max1:
            max3=max2
            max2=num
        elif max3<num<max2:
            max3=num
    print("Third largest element is: ",max3)
else:
    print("Enter 3 or more than 3 elements!")
