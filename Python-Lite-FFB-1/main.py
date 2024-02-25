# Списки и методы

# Вспомнить все!
word = "It's me"
print("длина word =", len(word))

name = word[-2:]
print(name)

# Про print
print("Покупки", "апельсин", "яблоко", "банан", sep="\n")

# Коллекции
# Список - изменяемая совокупность объектов
shop_lst = ['apple', 'banana', 'orange']  # список строк
primes = [1, 2, 3, 4, 5]  # список из int
bla_lst = [1, "Ha", "Гриша!", -0.509, []]  # список из разных объектов

# пустой список
empty_lst = []
print(type(empty_lst))
# # список из int

# про задачу 1
my_favorite_songs = 'Waste a Moment, Staying\' Alive, Start Me Up, New Salvation'
# Метод - специальные функции для конкретных типов данных
song_lst = my_favorite_songs.split(', ')
print(song_lst
      )  # ['Waste a Moment', "Staying' Alive", 'Start Me Up', 'New Salvation']

# индексация работает и для списков
print(song_lst[0], song_lst[3], song_lst[-2], song_lst[1], sep='\n')

# Методы списков
# метод добавления в конец списка
a = [1, 2]
a.append(5)
print(a)

a.append(-10)
print(a)

# Ошибка! Такого метода для int не существует всем привет от эльтуна
# 1.append(4)

group_list = group1.split(',')
print(group_list)
print(group_list[3])

# Приведем список покупок в магазине

shop_list = ['Картофель', 'Горошек', 'Рис', 'Хлеб']

# Измените список согласно пунктам задания
# Выведите результат каждого пункта на консоль по очереди

# а. Вставьте рыбу между горошком и рисом

# b. Добавьте фрукты из списка fruits в конец списка shop_list
fruits = ['Яблоко', 'Апельсин', 'Клубника']

# c. Удалите из списка shop_list картофель

# d. Какими по счету стоят хлеб и апельсин? Выведите номера на консоль в формате:
#   Номер "продукта" в списке - N

#############################################################
# Решение задачи
# а.
shop_list.insert(2, 'Рыба')
print(shop_list)

# Вопрос: почему не так?
# shop_list = shop_list.insert(2, 'Рыба')
# print(shop_list)

# b.
fruits = ['Яблоко', 'Апельсин', 'Клубника']
shop_list.extend(fruits)
print(shop_list)

# # Вопрос: что будет с append?
# shop_list.append(fruits)
# print(shop_list) # shop_list.extend(fruits)
# print(shop_list) # [... 'Хлеб', ['Яблоко', 'Апельсин', 'Клубника']]

# c.
# shop_list.remove('Картофель')
print(shop_list)

# Вопрос: какие еще методы удаления?
# element = shop_list.pop(0)
# print(element)

# del shop_list[0]
print(shop_list)

#d)

fname = "Хлеб"
sname = "Апельсин"
x = shop_list.index(fname)
y = shop_list.index(sname)

# Форматирование строк
# Вариант 1: Параметры print
print("Номер продукта", fname, "в списке ", x)
print("Номер продукта", sname, "в списке ", y)

# Вариант 2: метод format

print("Номер продукта '{}' в списке - №{}".format(fname, x))

# проблема
# url = "https://www.ranepa.ru/local/f&{}={},{}{}".format() ???

# Вариант 3: f-строки
print(f"Номер продукта '{fname}' в списке - №{x}")

# url = f"https://www.ranepa.ru/local/f&{x}={y},{z}{v}"
