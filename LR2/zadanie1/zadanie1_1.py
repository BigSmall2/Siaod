import datetime

print("Массив")
x = [1 ,2, 4,6,7,8,9,11,14,16,18,22,28,31,32,36,38,43,44,45,47,49,51]
print(x)

def binary_search(mas, element):
    start = 0
    end = len(mas)

    while (start <= end):

        mid = (start + end) // 2

        if element == mas[mid]:
            return mid

        if element < mas[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return "Элемент не найден"


start = datetime.datetime.now()      #время перед запуском бинарного поиска
print("Индекс искомого числа: ")
print(binary_search(x, 11))
print("Время поиска: ", datetime.datetime.now() - start)