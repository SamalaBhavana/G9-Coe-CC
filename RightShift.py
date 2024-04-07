#Right Shift
a=[int(x) for x in input("Enter the Array Elemnts separated by ',': ").split(',')]
n=len(a)
k=int(input("Enter the No.of Position: "))
if k<n:
    Arr=a[k:]
    for i in range(n-k,n):
        a[i]=a[i-(n-k)]
    for i in range(n-k):
        a[i]=Arr[i]
    print(a)
else:
    print("K should be less than no.of elements in array!")
