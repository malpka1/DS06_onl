# Давайте вновь поможем воспитательнице учить ребят числам. Напишите программу, которая строит числовой прямоугольник требуемого размера.
# Формат ввода В первой строке записано число N — высота числового прямоугольника. Во второй строке указано число width — ширина числового прямоугольника.
# Формат вывода
# Нужно вывести сформированный числовой прямоугольник требуемого размера. Чтобы прямоугольник был красивым,
# каждый его столбец должен обладать одинаковой шириной.
# Ввод
# 4
# 6
# Вывод
# 1 5  9 13 17 21
# 2 6 10 14 18 22
# 3 7 11 15 19 23
# 4 8 12 16 20 24


def task_8():
    height = int(input())
    width = int(input())
    rectangle = [
        [i + j for j in range(1, width * height, height)] for i in range(0, height)
    ]

    for row in rectangle:
        print(
            " ".join(
                "{:{digits}}".format(number, digits=len(list(str(height * width))))
                for number in row
            )
        )


if __name__ == "__main__":
    task_8()