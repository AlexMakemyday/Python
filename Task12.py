#Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
#Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
#а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму
#этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

import math
import random

x = random.randint(0,4)
y = random.randint(0,4)
print(x)
print(y)
s = x + y
p = x * y
print(s)
print(p)
y = int((s - math.sqrt(s**2-4*p))/2)
x = s - y
print("Первое число: " + str(x))
print("Второе число: " + str(y))


















