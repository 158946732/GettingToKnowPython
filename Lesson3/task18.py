# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 

import random
list = [0]
for i in range(19):
    list.append(i+random.randint(0,10))
print(list)

x = int(input("Введите число : "))
if x < list[0]:
     min = list[0] - x
else: min = x - list[0]
index = 0
for i in range(len(list)):
        if x > list[i]:
            count = x - list[i]
        else: count = list[i] - x
        if count < min:
            min = count
            index = i
print(f"Минимальное наиболее близкое по величине к числу {x} в массиве число {list[index]}")
    