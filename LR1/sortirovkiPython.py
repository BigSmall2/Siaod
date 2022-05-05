import random

import copy

import time

# Создания массива согласно условию
p = input('Введите да, если будете вносить свои значения для матрицы, и нет, если не будете: ')
if p == "да":
    m = int(input('m = '))
    n = int(input('n = '))
    min_limit = int(input("Минимальное число: "))
    max_limit = int(input("Максимальное число: "))
    Matrix = [[random.randint(min_limit, max_limit) for j in range(n)] for i in range(m)]
    print('Matrix:')
    for i in range(m):
        print(Matrix[i])
else:
    m = 5
    n = 5
    min_limit = 0
    max_limit = 10
    Matrix = [[random.randint(min_limit, max_limit) for j in range(n)] for i in range(m)]
    print('Matrix:')
    for i in range(m):
        print(Matrix[i])


# Сортировка выбором
def selectionSort(mas):
    for i in range(len(mas) - 1):
        minimum = mas[i]
        indexMinimuma = i
        for j in range(i+1, len(mas)):
            if mas[j] < minimum:
                minimum = mas[j]
                indexMinimuma = j
        if indexMinimuma != i:
            t = mas[i]
            mas[i] = mas[indexMinimuma]
            mas[indexMinimuma] = t
    return mas
print("Сортировка выбором")
for i in range(len(Matrix)):
    print(selectionSort(Matrix[i]))


# Сортировка вставкой
print("Сортировка вставкой")
def insertionSort(mas):
    for i in range(1, len(mas)):
        for j in range(i, 0, -1):
            if mas[j] < mas[j-1]:
                mas[j], mas[j-1] = mas[j-1], mas[j]
            else:
                break
    return mas

for i in range(len(Matrix)):
    print(insertionSort(Matrix[i]))


# Сортировка обменом
print("Сортировка обменом")
def bubbleSort (mas):
    for run in range(len(mas) - 1): #Внешний цикл, который позволяет сделать нужное количестко обходов
        for i in range(len(mas) - 1 - run):
            if mas[i] > mas[i+1]:
                mas[i], mas[i+1] = mas[i+1], mas[i]
    return mas

for i in range(len(Matrix)):
    print(bubbleSort(Matrix[i]))


print("Сортировка Шелла")
# Сортировка Шелла
def shellSort(matrix):
    n = len(matrix[0])
    m = len(matrix[0])
    for raw in range(n):
        l = m//2
        while l > 0:
            for i in range(l, m):
                x = matrix[raw][i]
                j = i
                while j >= l and matrix[raw][j-l] > x:
                    matrix[raw][j] = matrix[raw][j-l]
                    j -= l
                matrix[raw][j] = x
            l //= 2
    return matrix

for i in range(len(Matrix)):
    print(shellSort(Matrix))

#Быстрая сортировка
print("Быстрая сортировка")
def QuickSort(mas):
    if len(mas) <= 1:
        return mas
    else:
        q = random.choice(mas)
        L = [elem for elem in mas if elem < q]
        M = [q] * mas.count(q)
        R = [elem for elem in mas if elem > q]
        return QuickSort(L) + M + QuickSort(R)

for i in range(len(Matrix)):
    print(QuickSort(Matrix[i]))

#Турнирная сортировка
print("Турнирная сортировка")
def tournamentSort(matrix):
    tree = [None] * 2 * (len(matrix) + len(matrix) % 2)
    index = len(tree) - len(matrix) - len(matrix) % 2

    for i, v in enumerate(matrix):
        tree[index + i] = (i, v)

    for j in range(len(matrix)):
        n = len(matrix)
        index = len(tree) - len(matrix) - len(matrix) % 2
        while index > -1:
            n = (n + 1) // 2
            for i in range(n):
                i = max(index + i * 2, 1)
                if tree[i] != None and tree[i + 1] != None:
                    if tree[i][1] < tree[i + 1][1]:
                        tree[i // 2] = tree[i]
                    else:
                        tree[i // 2] = tree[i + 1]
                else:
                    tree[i // 2] = tree[i] if tree[i] != None else tree[i + 1]
            index -= n

        index, x = tree[0]
        matrix[j] = x
        tree[len(tree) - len(matrix) - len(matrix) % 2 + index] = None

def TournamentSort(matrix):
    for i in range(len(matrix)):
        tournamentSort(matrix[i])
    return matrix

print (TournamentSort(Matrix))


# Сортировка пирамидальная
print("Сортировка пирамидальная")
def heapify(matrix, n, i, row):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and matrix[row][i] < matrix[row][l]:
        largest = l
    if r < n and matrix[row][largest] < matrix[row][r]:
        largest = r

    if largest != i:
        matrix[row][i], matrix[row][largest] = matrix[row][largest], matrix[row][i]
        heapify(matrix, n, largest, row)

def heapSort(matrix):
    for row in range(len(matrix)):
        n = len(matrix[0])
        for i in range(n//2, -1, -1):
            heapify(matrix, n, i, row)
        for i in range(n-1, 0, -1):
            matrix[row][i], matrix[row][0] = matrix[row][0], matrix[row][i]
            heapify(matrix, i, 0, row)
    return matrix
print (heapSort(Matrix))

# Время подсчёта Сортировки выбором
Selection_sort_matrix = copy.deepcopy(Matrix)
start_time = time.time()
selectionSort(Selection_sort_matrix)
end_time_Selection_sort = time.time()-start_time
print("Сортировка простым выбором")
print("Время выполнения: ",end_time_Selection_sort,"sec")

# Время подсчёта Сортировки вставкой
insertion_sort_matrix = copy.deepcopy(Matrix)
start_time = time.time()
insertionSort(insertion_sort_matrix)
end_time_insertion_sort = time.time()-start_time
print("Сортировка вставкой")
print("Время выполнения: ",end_time_insertion_sort,"sec")

# Время подсчёта сортировки обменом
bubble_sort_matrix = copy.deepcopy(Matrix)
start_time = time.time()
bubbleSort(bubble_sort_matrix)
end_time_bubble_sort = time.time()-start_time
print("Сортировка обменом")
print("Время выполнения: ",end_time_bubble_sort,"sec")

# Время сортировки Шеллом
shellSort_matrix = copy.deepcopy(Matrix)
start_time = time.time()
shellSort(shellSort_matrix)
end_time_shell_Sort = time.time()-start_time
print("Шелл сортировка")
print("Время выполнения: ",'%.2f' %end_time_shell_Sort,"sec")

# Время турнирной сортировки
Tournament_sort_matrix = copy.deepcopy(Matrix)
start_time = time.time()
TournamentSort(Tournament_sort_matrix)
end_time_Tournament_sort = time.time()-start_time
print("Турнирная сортировка")
print("Время выполнения: ",end_time_Tournament_sort,"sec")

# Время быстрой сортировки
quick_sort_matrix = copy.deepcopy(Matrix)
start_time = time.time()
QuickSort(quick_sort_matrix)
end_time_quick_sort = time.time()-start_time
print("Быстрая сортировка")
print("Время выполнения: ",end_time_quick_sort,"sec")

# Время пирамидальной сортировки
heapSort_matrix = copy.deepcopy(Matrix)
start_time = time.time()
heapSort(heapSort_matrix)
end_time_heap_Sort = time.time()-start_time
print("Пирамидальная сортировка")
print("Время выполнения: ",end_time_heap_Sort,"sec")

# Время базовой сортировки
basic_sort = copy.deepcopy(Matrix)
start_time = time.time()
for i in range(len(basic_sort)):
    basic_sort[i].sort()
end_time_basic_sort = time.time()-start_time
print("Стандартная сортировка")
print("Время выполнения: ", end_time_basic_sort,"sec")