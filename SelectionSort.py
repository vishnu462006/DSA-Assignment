def Selection_Sort(arr):
   
     for i in range(0,len(arr)-1):
        min_index=i
        for j in range(i+1,len(arr)-1):
            if arr[j]<arr[min_index]:
                min_index=j
        if min_index!=i:
            arr[i],arr[min_index]=arr[min_index],arr[i]

arr=[23,56,43,1,67,890]
Selection_Sort(arr)
print(arr)
