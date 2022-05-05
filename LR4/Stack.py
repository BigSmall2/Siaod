class MyStack:

    def __init__(self):
        self.array = []

    def isempty(self):
        if self.array is None:
            return True
        if len(self.array) == 0:
            return True
        return False

    def add(self, element):
        self.array.append(element)

    def pop(self):
        return self.array.pop()

    def print(self):
        return (self.array)

    def __len__(self):
        return self.array.__len__()

    def peek(self):
        return self.array.__getitem__(len(self.array) - 1)


stack_my = MyStack()

print(stack_my.isempty())   # проверяем stack на пустоту
stack_my.add('2')           # добавляем элементы
stack_my.add('-8')
stack_my.add('366')
stack_my.add('1')
print(stack_my.print())     # Выводим элементы, находящиеся в stack
print("Удалённый элемент:", "'" + stack_my.pop() + "'")
print(stack_my.print())


#задача 3
A = MyStack()
B = MyStack()
C = MyStack()

file = open('task3_in.txt')

disks = int(file.readline())
for i in range(disks, 0, -1):
    A.add(i)

def move(a, b):
    # если исп.стек пустой и след. > 0
    if len(a) == 0 and len(b) > 0:
        #удаляем из b и перекладываем в a
        a.add(b.pop())
    elif len(a) > 0 and len(b) == 0:
        b.add(a.pop())
    #сравниваем первые элементы
    elif a.peek() > b.peek():
        a.add(b.pop())
    else:
        b.add(a.pop())

def task3(A, B, C):
    if disks % 2 == 0:
        while len(C) != disks:
            move(A, B)
            move(A, C)
            move(B, C)
    else:
        while len(C) != disks:
            move(A, C)
            move(A, B)
            move(B, C)

task3(A, B, C)

file = open('task3_out.txt', 'w')
while not C.isempty():
    file.write(str(C.pop()))



def task4(file_name):
    file = open(file_name)

    stack_t4 = MyStack()

    for line in file:
        for sym in line:
            if sym == '(':
                stack_t4.add("not_balanced")
            elif sym == ')':
                if stack_t4.isempty():
                    stack_t4.add("not_balanced")
                    break
                else:
                    stack_t4.pop()
    return stack_t4

stack_t4 = task4('task4_in.txt')

file = open('task4_out.txt', 'w')

if stack_t4.isempty():
    file.write("Balanced")
else:
    file.write("Not balanced")

#Символы, буквы, цифры
def task6(file_name):
    file = open(file_name)

    stack_symbols = MyStack()
    stack_numbers = MyStack()
    stack_other = MyStack()

    for line in file:
        for sym in line:
            if '9' >= sym[0] >= '0':
                stack_numbers.add(sym)
            elif 'A' <= sym[0] <= 'z':
                stack_symbols.add(sym)
            else:
                stack_other.add(sym)
    return stack_symbols, stack_numbers, stack_other

stack_symbols, stack_numbers, stack_other = task6('task6_in.txt')

stack_symbols_revers = MyStack()
stack_numbers_revers = MyStack()
stack_other_revers = MyStack()

while not stack_numbers.isempty():
    stack_numbers_revers.add(stack_numbers.pop())
while not stack_symbols.isempty():
    stack_symbols_revers.add(stack_symbols.pop())
while not stack_other.isempty():
    stack_other_revers.add(stack_other.pop())

file = open('task6_out.txt', 'w')

while not stack_numbers_revers.isempty():
    file.write(stack_numbers_revers.pop())
file.write('\n')
while not stack_symbols_revers.isempty():
    file.write(stack_symbols_revers.pop())
file.write('\n')
while not stack_other_revers.isempty():
    file.write(stack_other_revers.pop())

#Обратный порядок строк
def task8(file_name):
    file = open(file_name, encoding='utf-8')

    stack_t8_lines = MyStack()

    for line in file:
        stack_t8_lines.add(line)
    return stack_t8_lines


stack_t8_lines = task8('task8_in.txt')

file = open('task8_out.txt', 'w')

while not stack_t8_lines.isempty():
    file.write(stack_t8_lines.pop())