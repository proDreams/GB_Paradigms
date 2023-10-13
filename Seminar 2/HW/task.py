# Таблица умножения
# ● Условие
# На вход подается число n.
# ● Задача
# Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n.
# Обоснуйте выбор парадигм.
# ● Пример вывода:
# 1 * 1 = 1
# 1 * 2 = 2
# 1 * 3 = 3
# 1 * 4 = 4
# 1 * 5 = 5
# 1 * 6 = 6
# ..
# 1 * 9 = 9

START = 1
END = 11
HALF = 2

for i in range(START, END):
    for j in range(START, END // HALF + 1):
        print(f"{j:>2} X {i:>2} = {i * j:>2}", end="\t")
    print()
print()
for i in range(START, END):
    for j in range(END // HALF + 1, END):
        print(f"{j:>2} X {i:>2} = {i * j:>2}", end="\t")
    print()