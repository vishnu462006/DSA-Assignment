def Bubble_Sort(arr):
    n=len(arr)
    for i in range(n):
        swap=False
        for j in range(0,n-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swap=True
        if swap==False:
            break
arr=[23,54,876,9,2,40]
Bubble_Sort(arr)
print(arr)
