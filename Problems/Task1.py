def max_Perimeter(arr):
    arr.sort()
    for i in range(len(arr) - 3, -1, -1):
        if arr[i] + arr[i + 1] > arr[i + 2]:
            return arr[i] + arr[i + 1] + arr[i + 2]
    return 0


arr = [2, 1, 2]
print(max_Perimeter(arr))

arr = [1, 2, 1]
print(max_Perimeter(arr))

arr = [3, 2, 3, 4]
print(max_Perimeter(arr))

arr = [3, 6, 2, 3]
print(max_Perimeter(arr))