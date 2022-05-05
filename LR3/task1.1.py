# Алгоритм Кнута-Морриса-Пратта
import timeit

main_string = 'замок закрыт на большущий ЗАМОК'
string_to_find = 'ЗАМОК'
is_case_sensitive = False


print('Введите основную строку или оставьте пустой для строки по умолчанию: ')
buffer = input()
if buffer != '':
    main_string = buffer
    buffer = ''
else:
    print('По умолчанию: замок закрыт на большущий ЗАМОК')


print('Введите строку для поиска или оставьте пустой для строки по умолчанию: ')
buffer = input()
if buffer != '':
    string_to_find = buffer
    buffer = ''
else:
    print('По умолчанию: ЗАМОК')


print('Должен ли поиск быть чувствительным к регистру?')
buffer = input()
if buffer == 'да':
    is_case_sensitive = True


def prefix(s):
    str_prefix = [0]*len(s)   # массив
    for i in range(1, len(s)):
        j = str_prefix[i-1]
        while j > 0 and s[j] != s[i]:
            j = str_prefix[j-1]
        if s[j] == s[i]:
            j = j + 1
        str_prefix[i] = j
    return str_prefix


def kmp(s_main, s_sought, case_sensitive=True):
    if not case_sensitive:
        s_main = s_main.lower()
        s_sought = s_sought.lower()

    index = -1
    str_prefix = prefix(s_main)
    j = 0
    for i in range(len(s_sought)):  #идем по всей строке
        while j > 0 and s_main[j] != s_sought[i]:  #если не равны, то берем индекс для j из массива
            j = str_prefix[j-1]
        if s_main[j] == s_sought[i]:  #если равны, то проверяем следующие элементы. Если все элементы совпали, то все найдено
            j = j + 1
        if j == len(s_main):
            index = i - len(s_main) + 1 #индекс с которого начинается нужная подстрока
            break
    return index

print(kmp(string_to_find, main_string, is_case_sensitive))
print(kmp(string_to_find, main_string, False))

# Высчитываем время работы
print("Поиск Кнута-Морриса-Пратта " + str(timeit.timeit("kmp(string_to_find, main_string, is_case_sensitive)", number=1, globals=globals())))
print("Поиск по умолчанию " + str(timeit.timeit("main_string.find(string_to_find)", number=1, globals=globals())))



