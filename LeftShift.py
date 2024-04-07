#Left Shift
a=[int(x) for x in input("Enter the Array Elemnts separated by ',': ").split(',')]
n=len(a)
k=int(input("Enter the No.of Position: "))
if k<=n:
    Arr=a[:k]
    for i in range(n-k):
        a[i]=a[i+k]
    for i in range(n-k,n):
        a[i]=Arr[i-(n-k)]
    print(a)
else:
    print("K should be less than no.of elements in array!")
