import numpy
import timeit
import collections
import queue


# Первый способ (Сложнее). Плюс - легкая масштабируемость под свои задачи и нужды. Можно перенастраивать функции.
# Минус - сложность и возможность багов.

class CircularBuffer(object):
    buffer_methods = ('list', 'deque', 'roll')

    # Конструктор Буфера (Человек сам задает все числа)
    def __init__(self, buffer_size, buffer_method):
        self.content = None
        self.size = buffer_size
        self.method = buffer_method

    # Обновление списка
    def update(self, scalar):
        if self.method == self.buffer_methods[0]:
            # Используем list
            try:
                self.content.append(scalar)
                self.content.pop(0)
            except AttributeError:
                self.content = [0.] * self.size
        elif self.method == self.buffer_methods[1]:
            # Используем collections.deque
            try:
                self.content.append(scalar)
            except AttributeError:
                self.content = collections.deque([0.] * self.size,
                                                 maxlen=self.size)
        elif self.method == self.buffer_methods[2]:
            # Используем Numpy.roll
            try:
                self.content = numpy.roll(self.content, -1)
                self.content[-1] = scalar
            except IndexError:
                self.content = numpy.zeros(self.size, dtype=float)


# Второй способ (легче). Легкость - плюс данного способа, однако функциональная и масштабируемая часть намного слабее
# чем у первого способа. Порой, бывает нельзя подстроить под большие проекты и под большие нужды.


q1 = queue.Queue()
# Ниже приведены важные методы, доступные внутри класса Queue и Fifo Queue:
#
# put(element): Это поместит элемент в очередь.
# get(): Это вернет вам элемент из очереди.
# empty(): он вернет значение true, если очередь пуста, и значение false, если элементы присутствуют.
# qsize(): возвращает размер очереди.
# full(): возвращает значение true, если очередь заполнена, в противном случае значение false.
