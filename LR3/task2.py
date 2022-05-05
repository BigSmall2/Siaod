def print_pyatnashki(array):
    """
    Вывод пятнашек в красивом виде
    """
    int_separate = 0
    for x in array:
        if x <= 9:
            print(' ' + str(x), end=" ")
        else:
            print(x, end=" ")
        int_separate += 1
        if int_separate >= 4:
            int_separate = 0
            print()


def solvable(array): #решаемо или нет
    """
    Формуля для определения решаемости пятнашек взята из интернета
    :param array: наш массив для пятнашек
    :return: bool обозначающий, можно ли решить данные пятнашки
    """
    N = 0
    for x in array:
        if x == 0:
            N += array.index(0) // 4 + 1
        else:
            k = 0
            for i in range(array.index(x), len(array)):
                if array[i] < x and array[i] != 0:
                    k += 1
            N += k
    if N % 2 == 0:
        print(N)
        return True
    return False


arr_moves = []


def swap(array, empty_i, swap_this_i):
    """
    Функция для передвижения клеток
    :param array: наш массив для пятнашек
    :param empty_i: индекс пустой клетки
    :param swap_this_i: индекс клетки, которую мы собираемся двигать
    :return: индекс, на котором теперь находится пустая клетка
    """
    arr_moves.append(array[swap_this_i])
    array[empty_i], array[swap_this_i] = array[swap_this_i], array[empty_i]
    return swap_this_i


def rightmost_row_sort(array, empty_i):  #1 и 2 строка
    """
    Специальная последовательность перемещений, чтобы отсортировать цифры самого правого столбца (4,8)
    :param array: наш массив для пятнашек
    :param empty_i: индекс пустой клетки
    :return: индекс, на котором теперь находится пустая клетка
    """
    empty_i = swap(array, empty_i, empty_i - 1)
    empty_i = swap(array, empty_i, empty_i - 4)
    empty_i = swap(array, empty_i, empty_i - 1)
    empty_i = swap(array, empty_i, empty_i - 4)
    empty_i = swap(array, empty_i, empty_i + 1)
    empty_i = swap(array, empty_i, empty_i + 1)
    empty_i = swap(array, empty_i, empty_i + 4)
    empty_i = swap(array, empty_i, empty_i - 1)
    empty_i = swap(array, empty_i, empty_i - 4)
    empty_i = swap(array, empty_i, empty_i - 1)
    empty_i = swap(array, empty_i, empty_i + 4)


    return empty_i



def best_choice(best_array, origin, def_choice, choice2): #для 3 и 4 строки
    index_origin = best_array.index(origin)
    for index in range(index_origin, 16):
        if index >= len(best_array):
            index = 0
        if best_array[index] == def_choice:
            return def_choice
        if best_array[index] == choice2:
            return choice2
    return def_choice



def pyatnashki(array):
    if not solvable(array):
        return False

    arr_moves.clear()
    empty_i = -1
    for cur_numb in range(1, 9):

        cur_numb_i = -1
        for i in range(16):  # находим индекс рассматриваемой цифры
            if array[i] == cur_numb:
                cur_numb_i = i

        empty_i = array.index(0)
        desirable_i = cur_numb - 1

        # [1] Помещаем пустую клетку рядом с клеткой числа для перемещения
        row_of_our_number = (cur_numb_i // 4) + 1
        while abs(empty_i - cur_numb_i) != 4 and (abs(empty_i - cur_numb_i) != 1 or empty_i // 4 != cur_numb_i // 4):
            if empty_i // 4 + 1 < row_of_our_number:
                empty_i = swap(array, empty_i, empty_i + 4)
            elif cur_numb_i % 4 > empty_i % 4:
                empty_i = swap(array, empty_i, empty_i + 1)
            elif empty_i // 4 + 1 > row_of_our_number:
                empty_i = swap(array, empty_i, empty_i - 4)

            else:
                empty_i = swap(array, empty_i, empty_i - 1)

        # [2] Определяем куда нужно переместить наше значение и двигаем пустую клетку соответственно
        while cur_numb_i != desirable_i:

            if cur_numb_i % 4 > desirable_i % 4:
                if cur_numb_i // 4 + 1 == 4:  # находится на 4 ряду
                    if empty_i - cur_numb_i == 1:
                        empty_i = swap(array, empty_i, empty_i - 4)
                        empty_i = swap(array, empty_i, empty_i - 1)
                    if cur_numb_i - empty_i == 4:
                        empty_i = swap(array, empty_i, empty_i - 1)
                        empty_i = swap(array, empty_i, empty_i + 4)
                    if cur_numb_i - empty_i == 1:
                        empty_i = swap(array, empty_i, empty_i + 1)
                        cur_numb_i -= 1
                else:

                    if cur_numb_i - empty_i == 4:
                        if cur_numb_i % 4 == 3:
                            empty_i = swap(array, empty_i, empty_i - 1)
                            empty_i = swap(array, empty_i, empty_i + 4)
                        else:
                            empty_i = swap(array, empty_i, empty_i + 1)
                            empty_i = swap(array, empty_i, empty_i + 4)
                    if empty_i - cur_numb_i == 1:
                        empty_i = swap(array, empty_i, empty_i + 4)
                        empty_i = swap(array, empty_i, empty_i - 1)
                    if empty_i - cur_numb_i == 4:
                        empty_i = swap(array, empty_i, empty_i - 1)
                        empty_i = swap(array, empty_i, empty_i - 4)
                    if cur_numb_i - empty_i == 1:
                        empty_i = swap(array, empty_i, empty_i + 1)
                        cur_numb_i -= 1

            elif cur_numb_i % 4 < desirable_i % 4:
                if cur_numb_i // 4 + 1 == 4:  # находится на 4 ряду
                    if cur_numb_i - empty_i == 1:
                        empty_i = swap(array, empty_i, empty_i - 4)
                        empty_i = swap(array, empty_i, empty_i + 1)
                    if cur_numb_i - empty_i == 4:
                        empty_i = swap(array, empty_i, empty_i + 1)
                        empty_i = swap(array, empty_i, empty_i + 4)
                    if empty_i - cur_numb_i == 1:
                        empty_i = swap(array, empty_i, empty_i - 1)
                        cur_numb_i += 1
                else:
                    if cur_numb_i - empty_i == 4:
                        empty_i = swap(array, empty_i, empty_i + 1)
                        empty_i = swap(array, empty_i, empty_i + 4)
                    if cur_numb_i - empty_i == 1:
                        empty_i = swap(array, empty_i, empty_i + 4)
                        empty_i = swap(array, empty_i, empty_i + 1)
                    if empty_i - cur_numb_i == 4:
                        empty_i = swap(array, empty_i, empty_i + 1)
                        empty_i = swap(array, empty_i, empty_i - 4)
                    if empty_i - cur_numb_i == 1:
                        empty_i = swap(array, empty_i, empty_i - 1)
                        cur_numb_i += 1

            else:
                if cur_numb_i % 4 == 3:  # Находится на 4 столбце
                    if cur_numb_i // 4 > desirable_i // 4 + 1:
                        if empty_i - cur_numb_i == 4:
                            empty_i = swap(array, empty_i, empty_i - 1)
                            empty_i = swap(array, empty_i, empty_i - 4)
                        if cur_numb_i - empty_i == 1:
                            empty_i = swap(array, empty_i, empty_i - 4)
                            empty_i = swap(array, empty_i, empty_i + 1)
                        if cur_numb_i - empty_i == 4:
                            empty_i = swap(array, empty_i, empty_i + 4)
                            cur_numb_i -= 4
                    else:
                        if cur_numb_i - empty_i == 4:
                            empty_i = swap(array, empty_i, empty_i + 4)
                            cur_numb_i = desirable_i
                            continue
                        if cur_numb_i - empty_i == 1:
                            empty_i = swap(array, empty_i, empty_i + 4)
                            empty_i = swap(array, empty_i, empty_i + 1)
                        if empty_i - cur_numb_i == 4:
                            empty_i = rightmost_row_sort(array, empty_i)
                            cur_numb_i = desirable_i
                else:
                    if cur_numb_i // 4 > desirable_i // 4:
                        if cur_numb_i // 4 + 1 == 4:  # находится на 4 ряду
                            if cur_numb_i - empty_i == 1:
                                empty_i = swap(array, empty_i, empty_i - 4)
                                empty_i = swap(array, empty_i, empty_i + 1)
                            if empty_i - cur_numb_i == 1:
                                empty_i = swap(array, empty_i, empty_i - 4)
                                empty_i = swap(array, empty_i, empty_i - 1)
                            if cur_numb_i - empty_i == 4:
                                empty_i = swap(array, empty_i, empty_i + 4)
                                cur_numb_i -= 4
                        else:
                            if cur_numb_i - empty_i == 1:
                                empty_i = swap(array, empty_i, empty_i + 4)
                                empty_i = swap(array, empty_i, empty_i + 1)
                            if empty_i - cur_numb_i == 4:
                                empty_i = swap(array, empty_i, empty_i + 1)
                                empty_i = swap(array, empty_i, empty_i - 4)
                            if empty_i - cur_numb_i == 1:
                                empty_i = swap(array, empty_i, empty_i - 4)
                                empty_i = swap(array, empty_i, empty_i - 1)
                            if cur_numb_i - empty_i == 4:
                                empty_i = swap(array, empty_i, empty_i + 4)
                                cur_numb_i -= 4
    # [3] 3 и 4 строки
    sought_arr = [9, 10, 11, 12, 15, 14, 13]  # массив, который мы желаем в итоге получить из двух строк
    while True:
        if empty_i == 8:
            empty_i = swap(array, empty_i, empty_i + 1)
        elif empty_i == 9:
            index = array.index(best_choice(sought_arr, array[8], array[10], array[13]))
            if index == 13 and sought_arr.index(array[8]) > sought_arr.index(array[14]):
                empty_i = swap(array, empty_i, index)
                empty_i = swap(array, empty_i, empty_i - 1)
            else:
                empty_i = swap(array, empty_i, index)

        elif empty_i == 10:
            index = array.index(best_choice(sought_arr, array[9], array[11], array[14]))
            if index == 14 and sought_arr.index(array[9]) > sought_arr.index(array[15]):
                empty_i = swap(array, empty_i, index)
                empty_i = swap(array, empty_i, empty_i - 1)
                empty_i = swap(array, empty_i, empty_i - 1)
                empty_i = swap(array, empty_i, empty_i - 4)
                empty_i = swap(array, empty_i, empty_i + 1)
                empty_i = swap(array, empty_i, empty_i + 1)

            else:
                empty_i = swap(array, empty_i, index)

        elif empty_i == 11:
            empty_i = swap(array, empty_i, empty_i + 4)
        elif empty_i == 12:
            empty_i = swap(array, empty_i, empty_i - 4)
        elif empty_i == 13:
            index = array.index(best_choice(sought_arr, array[14], array[12], array[9]))
            if index == 9 and sought_arr.index(array[14]) > sought_arr.index(array[8]):
                empty_i = swap(array, empty_i, index)
                empty_i = swap(array, empty_i, empty_i + 1)
                empty_i = swap(array, empty_i, empty_i + 1)
                empty_i = swap(array, empty_i, empty_i + 4)
                empty_i = swap(array, empty_i, empty_i - 1)
                empty_i = swap(array, empty_i, empty_i - 1)
            else:
                empty_i = swap(array, empty_i, index)

        elif empty_i == 14:
            index = array.index(best_choice(sought_arr, array[15], array[13], array[10]))
            if index == 10 and sought_arr.index(array[15]) > sought_arr.index(array[9]):
                empty_i = swap(array, empty_i, index)
                empty_i = swap(array, empty_i, empty_i + 1)
                empty_i = swap(array, empty_i, empty_i - 4)
                empty_i = swap(array, empty_i, empty_i - 1)
            else:
                empty_i = swap(array, empty_i, index)

        else:
            if array[8] == 9 and array[9] == 10 and array[10] == 11 and array[11] == 12 and array[12] == 13 and array[13] == 14 and  array[14] == 15 and array[15] == 0:
                print_pyatnashki(array)
                return arr_moves
            empty_i = swap(array, empty_i, empty_i - 1)


pyatnashki_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 14, 0]
arr1 = [10, 6, 4, 13, 3, 5, 14, 1, 12, 8, 15, 0, 7, 11, 2, 9]
arr2 = [15, 1, 11, 7, 10, 4, 12, 14, 2, 8, 5, 13, 0, 6, 3, 9]
arr3 = [8, 15, 10, 5, 6, 9, 13, 4, 2, 1, 12, 7, 3, 0, 11, 14]
arr4 = [12, 2, 7, 3, 11, 6, 15, 4, 10, 5, 1, 9, 14, 13, 8, 0]

print(pyatnashki(arr1))
print(pyatnashki(arr2))
print(pyatnashki(arr4))
print(pyatnashki(arr4))
print(pyatnashki(pyatnashki_array))