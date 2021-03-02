"""
Очень часто для ввода с клавиатуры в python используется функция input() которая может вывести сообщения на экран
и возвращает то что ввел пользователь с клавиатуры:

value = input("Enter some value: ")

однако она всегда возвращает тип "символьная строка" - string, что требует несомненно применить "преобразование"
типа - для дальнейшего применения вводимого значения в том или ином случае.

Для облегчения разработки, требуется создать 3 простые функции, каждая из которых должна позволить ввести с клавиатуры
значение и вернуть значение уже "преопразованым" в нужный тип данных. Их имена:

inputInt( message )
inputFloat( message )
inputBoolean( message )

каждая из них должна внутри себя использовать "input()"
каждая преобразует значение в тип который упоминается в ее название
После того как код функций будет создан, можно запустить для проверки такого рода код:

n = inputInt("Enter the first integer: ")
m = inputInt("Enter the second integer: ")
print( n + m )
"""

# def inputInt(message):
#     int_number = input(message)
#     i = int(int_number)
#     return i

# def inputInt(message):
#     int_number = input(message)
#     if int_number.isdigit():
#         i = int(int_number)
#         return i
#     else:
#         print("It isn't a digital")


def inputInt(message):
    int_number = input(message)
    f = float(int_number)
    i = int(f)
    return i

def inputFloat(message):
    float_number = input(message)
    f = float(float_number)
    return f

def inputBoolean(message):
    bool_number = input(message)
    if bool_number == "True":
        return True
    if bool_number == "False":
        return False

# n = inputInt("Enter the first integer: ")
# m = inputInt("Enter the second integer: ")
# print(n+m)
#
# n = inputFloat("Enter the first float number: ")
# m = inputFloat("Enter the second float number: ")
# print(n+m)

n = inputBoolean("Enter the first boolean: ")
m = inputBoolean("Enter the second boolean: ")
print(n)
print(m)
# i = n + m
# print(i)
# print(type(i))
#
# print("**************************************")
#
# b = bool(0)
# print(b)
# print(type(b))