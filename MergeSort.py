def merge_sort(array):
    if len(array) > 1:
        midpoint = len(array) // 2  
        left_half = array[:midpoint]
        right_half = array[midpoint:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1

array_size = int(input("Enter the array length: "))
array = []
for i in range(array_size):
    number = int(input(f"Enter the element {i}: "))
    array.append(number)

print("Original array:", array)
merge_sort(array)
print("Sorted array:", array)
