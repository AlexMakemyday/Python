# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются
# в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
#№ m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input("Ввести количество элементов 1ого множества: "))
m = int(input("Ввести количество элементов 2ого множества: "))

list_1 = input("Введите " + str(n) + " числа/чисел через пробел: ").split(' ')[:n]
list_2 = input("Введите " + str(n) + " числа/чисел через пробел: ").split(' ')[:m]
set_1 = set(list_1)
set_2 = set(list_2)
#print(set_1)
#print(set_2)
final = set_1.intersection(set_2)
#print(final)
list_1 = list(final)
#print(list_1)
#print(type(list_1))
list_1.sort()
for i in list_1:
    print(i, end=' ')



