# Переменные и строки

# переменные - ярлыки для хранения результатов операции
#num = 2 + 2
#print(num)

# результаты длинных вычислений можно записывать в переменные
# print(((20 * 5)**2) / (1004**2 + 500**4))

# запишем результат в переменную result
#result = ((20 * 5)**2) / (1004**2 + 500**4)
#print(result)

# Строки
# различия в кавычках
word = "Hello, World!"
word = 'Hello, World!'
word = """Hello, world!"""
"""
Copyright 2013 Nikita Pyshkov
bla-bla
"""

print("Стоять, 'груши околачивать'👵")
# или
print('Стоять, \'груши околачивать\'👵')

# тип данных - str
print(type(word))
new_word = str(123)
new_num = int("1205")

# Множественное присвоение
# длинная запись
fvar = 5
svar = 10
tvar = 15

# запись в одну строку
fvar, svar, tvar = 5, 10, 15

print(fvar, svar, tvar)

# присвоение
var = 5 * (5 // 2)
печатай = print
печатай(var)

# операции со строками
print(word)
print(word + " " + "Hello")
print(word * 2)

# длина строки
print(len(word))

# задача на операции со строками
string = '0 1 2 '
print(type(string))
print(
    string * 2,  # 0 1 2 0 1 2
    string * 0,  # пустая строка ""
    string * -1,  # пустая строка ""
)

# пустая строка
empty_str = ""

# Индексация строк
word = "Hello, World!"
# обратимся к элементу H
print(word[0])

# обратимся к элементу d
print(word[-2])

# вырезать слово hello
print(word[0:5])

# вырезать слово world
print(word[7:-1])

# и срезы тоже можно складывать
print(word[7:-1] + word[0:5])
print(word[7:len(word)])

# можно не указывать 0 и последний индексы
print(word[:5] + word[6:])  # HelloWorld

# шаг среза
print(word[0:6:2])  # Hlo

# инверсия строки
print(word[::-1])

# Задача
# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.


