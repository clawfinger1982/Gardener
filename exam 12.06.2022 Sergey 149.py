# 1. Напишите функцию, которая будет принимать номер кредитной карты и
# показывать только последние 4 цифры. Остальные цифры должны заменяться
# звездочками
# card=('1234567890123456')
# def c_card(card):
#     return '*' * len(card[:-4]) + card[-4:]
# print(c_card(card))



# 2. Напишите функцию, которая проверяет: является ли слово палиндромом
# word='palindrom'
# # word='palap' # для проверки
# def Palindrom_check(word):
#     if word[::-1].startswith(word):
#         return True
#     else:
#         return False
# print(Palindrom_check(word))


# 3. Решите задачу
#
# Класс Tomato:
# 1. Создайте класс Tomato
import random
class Tomato:
# 2. Создайте статическое свойство states, которое будет содержать все стадии
# созревания помидора
    states={1:'vysazhen rostok',2:'est plod', 3:'plod vyros', 4:'plod sozrel'}
# 3. Создайте метод __init__(), внутри которого будут определены два динамических
# protected свойства: 1) _index - передается параметром и 2) _state - принимает первое
# значение из словаря states
    def __init__(self, index):
        self._index = index
        self._state = 0
# 4. Создайте метод grow(), который будет переводить томат на следующую стадию
# созревания
    def grow(self):
        self._next_stage()
        print('rastet, zreet')
    def _next_stage(self):
        if self._state < 4:
            self._state += 1
        print(f'Tomato {self._index+1} -- {Tomato.states[self._state]}')
# 5. Создайте метод is_ripe(), который будет проверять, что томат созрел (достиг
# последней стадии созревания)
    def is_ripe(self):
        if self._state==4:
            return True
        else:
            return False
# Класс TomatoBush
# 1. Создайте класс TomatoBush
# 2. Определите метод __init__(), который будет принимать в качестве параметра
# количество томатов и на его основе будет создавать список объектов класса
# Tomato. Данный список будет храниться внутри динамического свойства tomatoes.
class TomatoBush:
    def __init__(self, qtomatoes): #Число томатов на кусте
        self.tomatoes=[Tomato(i) for i in range(0, qtomatoes)]
# 3. Создайте метод grow_all(), который будет переводить все объекты из списка
# томатов на следующий этап созревания
    def grow_all(self):
        for i in self.tomatoes:
            i.grow()
# 4. Создайте метод all_are_ripe(), который будет возвращать True, если все томаты из
# списка стали спелыми
    def all_are_ripe(self):
        print('Proverka zrelosti')
        return all([i.is_ripe() for i in self.tomatoes])
# 5. Создайте метод give_away_all(), который будет чистить список томатов после
# сбора урожая
    def give_away_all(self):
        self.tomatoes.clear()
        # print('Net tomatov')
# Класс Gardener
# 1. Создайте класс Gardener
# 2. Создайте метод __init__(), внутри которого будут определены два динамических
# свойства: 1) name - передается параметром, является публичным и 2) _plant -
# принимает объект класса Tomato, является protected
class Gardener:
    def __init__(self, name, plant):
        print('Sadim rostok')
        self.name = name
        self._plant = plant
# 3. Создайте метод work(), который заставляет садовника работать, что позволяет
# растению становиться более зрелым
    def work(self):
        print('Polivaem, udobraem')
        self._plant.grow_all()
        print('Polili, udobrili')
# 4. Создайте метод harvest(), который проверяет, все ли плоды созрели. Если все -
# садовник собирает урожай. Если нет - метод печатает предупреждение.
    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Tomaty sozreli i sobrany')
        else:
            print('Tomaty esche ne sozreli')
# 5. Создайте статический метод knowledge_base(), который выведет в консоль справку
# по садоводству.
    @staticmethod
    def knowledge_base():
        print('Spravka po sadovodstvu: Kolhoz imeni Michurina')
# Тесты:
# 1. Вызовите справку по садоводству
# 2. Создайте объекты классов TomatoBush и Gardener

tomatobush=TomatoBush(random.randint(1,8)) # число томатов на кусте, случайно
# tomatobush=TomatoBush(2) # число томатов на кусте
gardener=Gardener('Michurin', tomatobush)
gardener.knowledge_base()
# 3. Используя объект класса Gardener, поухаживайте за кустом с помидорами
# 4. Попробуйте собрать урожай
# 5. Если томаты еще не дозрели, продолжайте ухаживать за ними
# 6. Соберите урожай
gardener.harvest()
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()




