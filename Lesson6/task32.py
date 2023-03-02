# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random 
list1 = [] 
for i in range(20):     
    i = random.randint(-10,10)     
    list1.append(i) 
print(list1) 
list2 = []
min = int(input('Введите минимальное значение диапазона: '))
max = int(input('Введите максимальное значение диапазона: '))
for i in range(len(list1)):
    if list1[i] >= min and list1[i]<= max:
        list2.append(i)
print(list2)
