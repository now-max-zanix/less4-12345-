import time

def mno():
    string1 = input("\nВведите первый список:")
    list1 = list(string1)
    print(list1)
    set1 = set(list1)
    print(set1)
    time.sleep(2)

def zad4():
    open_list = ["[","{","(","<"]
    close_list = ["]","}",")",">"]

    text = input("\nВведите данные:")
    def proverka(text):
        stack = []
        for i in text:
            if i in open_list:
                stack.append(i)
            elif i in close_list:
                ind = close_list.index(i)
                if stack and (open_list[ind] == stack[len(stack)-1]):
                    stack.pop()
                else:
                    return "Не корректно раставлены скобки"
        if len(stack) == 0:
            return "Ошибок нет"
        else:
            return "Не хватает скобок(ки)"
    print(proverka(text))
    time.sleep(2)


while True:
    print(
"""
Выберите задачу.
Удалить из списка повторяющиеся элементы:    1
Правильно ли расставлены скобки:             2
Выход:                                       Enter
"""
    )
    next_step = input("\nВведите: ")
    if not next_step:
        print("Удачи...")
        break
    elif next_step == "1":
        mno()
    elif next_step == "2":
        zad4()
    else:
        print("Повторите ввод")