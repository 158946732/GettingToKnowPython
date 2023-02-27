# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.

list1 = input("Введите 1 набор целых чисел(можно повторяющихся): ").split()
list2 = input("Введите 2 набор целых чисел(можно повторяющихся): ").split()
newList1 = []
newList2 = []
list3 = []
for i in set(list1):
    newList1.append(i)
newList1.sort()
for i in set(list2):
    newList2.append(i)
newList2.sort()
print(newList1)
print(newList2)
for i in range(len(newList1)):
    for j in range(len(newList2)):
        if newList1[i] == newList2[j]:
            list3.append(newList1[i])
# list3 = newList1.intersection(newList2) - не сработало
print(list3)