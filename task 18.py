# Задача 18: Требуется найти в массиве A[0..N-1] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел A[i]. 
# Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

N = int(input('Введите размер массива - '))
numbers = [0]*N
for i in range(len(numbers)):
    numbers[i] = int(input(f"Введите {i} элемент из списка: "))
print(numbers)
x = int(input('Введите искомое число - '))

i = 0
while x == numbers[i]:
    i += 1
seach_num = numbers[i]

for  list in numbers:
    if list != x:
        if abs(list - x) < abs(seach_num - x):
            seach_num = list
print(f"Ближайшее число к числу {x} это {seach_num}")



