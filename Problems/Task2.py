def dualComp(a, b):
    ab = int(str(a) + str(b))
    ba = int(str(b) + str(a))
    if ab > ba:
        return True
    else:
        return False

def sortArr(arr):
    for i in range(len(arr) - 1):
        max = i
        for j in range(i + 1, len(arr)):
            if not dualComp(arr[max], arr[j]):
                max = j
        arr[i], arr[max] = arr[max], arr[i]

def max_Number(nums):
    sortArr(nums)
    return ''.join(str(e) for e in nums)


print(max_Number([10, 2]))
print(max_Number([3, 30, 34, 5, 9]))
print(max_Number([1]))
print(max_Number([10]))