import random
import hashlib
from collections import deque
import time
import copy

def genMat():
    while True:
        try:
            m = int(input("Введите кол-во элементов в матрице: "))
        except:
            print("Ошибка, введено не целое число")
            continue
        break
    while True:
        try:
            min_limit = int(input("Введите минимальное значение в матрице: "))
        except:
            print("Ошибка, введено не целое число")
            continue
        break
    while True:
        try:
            max_limit = int(input("Введите максимальное значение в матрице: "))
        except:
            print("Ошибка, введено не целое число")
            continue
        break
    if min_limit > max_limit:
        min_limit = -250
        max_limit = 1012
    matrix = [random.randint(min_limit, max_limit) for j in range(m)]
    return(matrix)


matrix = genMat()
matrix.sort()
print(matrix)


# Простое рехэширование
def simple_re_hash(sl, matrix):
    for j in range(0, len(matrix)):
        temp = matrix[j]
        i = 1
        while True:
            if hash(temp) not in sl.keys():
                sl[hash(temp)] = matrix[j]
                break
            else:
                while hash(temp) + i in sl.keys(): #пока не найдем свободный хэш номер прибавляем 1
                    i += 1
                sl[hash(matrix[j] + i)] = matrix[j]
                break


# Рехэширование с помощью псевдослучайных чисел
def rand_re_hash(sl, matrix):
    for j in range(0, len(matrix)):
        temp = matrix[j]
        while True:
            if hash(temp) not in sl.keys():
                sl[hash(temp)] = matrix[j]
                break
            else:
                temp = matrix[j] + (random.randint(0, 1000))

#Метод цепочек
def chain_method(sl, matrix):
    for j in range(0, len(matrix)):
        temp = matrix[j]
        if hash(temp) in sl.keys():
            if isinstance(sl[hash(temp)], deque):
                sl[hash(temp)].append(matrix[j])
            else: # создаем очередь под этим хэш номером
                a = sl[hash(temp)]
                sl[hash(temp)] = deque([a, matrix[j]])
        else:
            sl[hash(temp)] = matrix[j]


print("Метод простого рехеширования")
slsimple = dict()
simple_re_hash(slsimple, matrix)
stroksimple = str(slsimple.items())
print(stroksimple)
print("Метод простого рехеширования с использованием псевдослучайных чисел")
slrand = dict()
rand_re_hash(slrand, matrix)
strokrand = str(slrand.items())
print(strokrand)
print("Метод рехеширования с использованием цепочек")
slrchain = dict()
chain_method(slrchain, matrix)
strokchain = str(slrchain.items())
print(strokchain)