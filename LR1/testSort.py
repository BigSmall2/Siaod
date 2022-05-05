import random
from random import randint
import copy
import math
import time


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

