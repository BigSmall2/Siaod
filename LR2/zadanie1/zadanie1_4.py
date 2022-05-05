import time
import copy

print("Массив")
arr = [1, 2, 4, 6, 7, 8, 9, 11, 14, 16, 18, 22, 28, 31, 32, 36, 38, 43, 44, 45, 47, 49, 51]
print(arr)


def InterpolationSearch(lys, val):
    low = 0      #индекс 1-го элемента
    high = (len(lys) - 1)  #индекс последнего элемента

    while low <= high and val >= lys[low] and val <= lys[high]:
        index = low + int(((float(high - low) / (lys[high] - lys[low])) * (val - lys[low]))) #Формула для нахождения индекса

        if lys[index] == val:
            return index

        if lys[index] < val:
            low = index + 1

        else:
            high = index - 1

    return -1


print("Интерполяционный поиск")
print("Введите элемент, который хотите найти: ")
element = int(input())
mas_inter = copy.deepcopy(arr)
start_time_inter = time.time()
b = InterpolationSearch(arr, element)
end_time_inter = time.time()-start_time_inter
if b == -1:
    print("Искомого числа в массиве нет")
else:
    print("Индекс: ", b)
print("Время работы: ", end_time_inter)