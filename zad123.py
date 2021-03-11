import random
import time
import collections
def num():

    a = []
    while True:
        k = input("\nСколько вывести чисел:")
        if k.isdigit():
            k = int(k)
            for i in range(k):
                a.append(random.randint(-10, 30))
                b = len(a)
            print(a)
            b = len(a)
            for i in range(b-1):
                for j in range(b-i-1):
                        if a[j] > a[j+1]:
                            a[j], a[j+1] = a[j+1], a[j]
            print(a)
            break
        else:
            print("Error- введите число")
    time.sleep(2)

def num2():
    string1 = input("\nВведите первый список:")
    string2 = input("Введите второй список:")

    list1 = list(string1)   
    list2 = list(string2)
    print("Список1", list1, "\nСписок2", list2)
    set1 = set(list1)
    set2 = set(list2)
    print("Множество 1:", set1)
    print("Множество 2:", set2 )
    if set1 == set2:
        print("\nСовпадает\n")
        time.sleep(4)
    else:
        print("\nНесовпадает\n") 
        time.sleep(2)
def num3():
    while True:
        pr = input("\nВедите предложение:")
        if pr.isdigit():
            print("Error")
            continue
        else:
            pr =str(pr)
            req = collections.Counter(pr)
            print("\nКоличество символов:\n", str(req))
            time.sleep(2)
            break
        

while True:
    print(
"""
Выберите задачу.
Сортировка Пузырьковым методом:    1
Сравнить множества списка:         2
Определить частоту всех символов:  3
Выход:                             Enter
"""
    )
    next_step = input("\nВведите: ")
    if not next_step:
        print("Удачи...")
        break
    elif next_step == "1":
        num()
    elif next_step == "2":
        num2()
    elif next_step == "3":
        num3()
    else:
        print("Повторите ввод")