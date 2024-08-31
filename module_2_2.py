name = 'Задача "Все ли равны?": Введи 3 целых числа.'
print(name)
first = int(input())
second = int(input())
third = int(input())
if first == second and second == third and third == first:
    print(3)
elif first != second and second != third and third != first:
    print(0)
else:
    print(2)
