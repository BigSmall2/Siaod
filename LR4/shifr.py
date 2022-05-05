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