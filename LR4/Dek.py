class DeQue:

    def __init__(self):
        self.array = []

    def empty(self):
        if self.array is None:
            return True
        if len(self.array) == 0:
            return True
        return False

    def addbeginning(self, element):
        self.array.insert(0, element)

    def addend(self, element):
        self.array.append(element)

    def popbeginning(self):
        return self.array.pop(0)

    def popend(self):
        return self.array.pop()

    def peekbeginning(self):
        return self.array.__getitem__(0)

    def peekend(self):
        return self.array.__getitem__(len(self.array) - 1)

    def print(self):
        return  (self.array)


deque_my = DeQue()

print(deque_my.empty())

deque_my.addbeginning('2')
deque_my.addbeginning('3')
deque_my.addend('5')
deque_my.addend('6')
print(deque_my.print())

print("Удалённый c начала элемент:", "'" + deque_my.popbeginning() + "'")
print("Удалённый c конца элемент:", "'" + deque_my.popend() + "'")
print(deque_my.print())

#Задание №1 Книги в алфавитном порядке
def task1(file_name):
    file = open(file_name, encoding ='utf-8')
    deque_t1_buffer = DeQue()
    deque_t1_main = DeQue()

    for line in file:
        deque_t1_buffer.addend(line)

    while not deque_t1_buffer.empty():     #Пока список не пуст, то проверяем
        if deque_t1_main.empty():
            deque_t1_main.addend(deque_t1_buffer.popend())

        if deque_t1_main.peekend()[0] <= deque_t1_buffer.peekend()[0]:
            deque_t1_main.addend(deque_t1_buffer.popend())
        elif deque_t1_main.peekbeginning()[0] > deque_t1_buffer.peekend()[0]:
            deque_t1_main.addbeginning(deque_t1_buffer.popend())
        else:
            deque_t1_buffer.addbeginning(deque_t1_main.popbeginning())
    return deque_t1_main


deque_t1_main = task1('task1_in.txt')

file = open('task1_out.txt', 'w')  # w - открытие на запись файла
while not deque_t1_main.empty():
    file.write(deque_t1_main.popbeginning())



#Шифрование
def task2(file_name):
    file = open(file_name, encoding='utf-8')

    deque_t2_encoder = DeQue()
    # формируем дек
    for i in range(32):
        deque_t2_encoder.addend(str(ord("а") + i))
    deque_t2_encoder.addend(str(ord(" ")))

    s_message = ''
    for line in file:
        for sym in line:
            while sym != chr(int(deque_t2_encoder.peekend())):
                deque_t2_encoder.addbeginning(deque_t2_encoder.popend())

            deque_t2_encoder.addbeginning(deque_t2_encoder.popend())
            deque_t2_encoder.addbeginning(deque_t2_encoder.popend())
            s_message += chr(int(deque_t2_encoder.peekend()))
    return s_message

s_message = task2('task2_in.txt')
file = open('task2_out.txt', 'w')
file.write(s_message)

#Квадратные скобки
def task5(file_name):
    file = open(file_name)

    deque_t5 = DeQue()

    for line in file:
        for sym in line:
            if sym == '[':
                deque_t5.addbeginning("not_balanced")
            elif sym == ']':
                if deque_t5.empty():
                    deque_t5.addbeginning("not_balanced")
                    break
                else:
                    deque_t5.popbeginning()
    return deque_t5


deque_t5 = task5('task5_in.txt')
file = open('task5_out.txt', 'w')

if deque_t5.empty():
    file.write("Balanced")
else:
    file.write("Not balanced")

#отрицательные и положительные числа
def task7(file_name):
    file = open(file_name)

    deque_t7_neg = DeQue()
    deque_t7_pos = DeQue()

    f_positive = True
    for line in file:
        for sym in line:
            if sym == '-':
                f_positive = False
                continue
            if sym != ' ':
                if f_positive:
                    deque_t7_pos.addbeginning(sym)
                else:
                    deque_t7_neg.addbeginning('-' + sym)
                    f_positive = True
    return deque_t7_neg, deque_t7_pos


deque_t7_neg, deque_t7_pos = task7('task7_in.txt')

deque_t7_neg_revers = DeQue()
deque_t7_pos_revers = DeQue()

while not deque_t7_neg.empty():
    deque_t7_neg_revers.addbeginning(deque_t7_neg.popbeginning())
while not deque_t7_pos.empty():
    deque_t7_pos_revers.addbeginning(deque_t7_pos.popbeginning())

file = open('task7_out.txt', 'w')

while not deque_t7_neg_revers.empty():
    file.write(deque_t7_neg_revers.popbeginning() + ' ')
file.write('\n')
while not deque_t7_pos_revers.empty():
    file.write(deque_t7_pos_revers.popbeginning() + " ")