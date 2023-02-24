# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].

import random
list = [0]
for i in range(19):
    list.append(i+random.randint(0,10))
print(list)
count = 0
x = int(input("Введите целое число: "))
for i in range(len(list)):
    if x == list[i]:
        count += 1
print(f"Ваше число встречается в массиве {count} раза")
