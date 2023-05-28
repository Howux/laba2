def one():
    password = str(input("Введите пароль: "))

    print("Введите пароль еще раз")

    password2 = str(input(""))

    if password == password2:
        print("Пароль принят")
    else:
        print("Пароль не принят")


def two():
    number = int(input("Введите номер места (до 54): "))

    if number > 54:
        return print("Неверный номер места")

    if number % 2 == 0 and number < 37:
        print("Ваше место в купе верхнее")
    else:
        if number % 2 == 0 and number >= 37:
            print("Ваше место боковое верхнее")

    if number % 2 != 0 and number < 37:
        print("ваше в купе место нижнее")
    else:
        if number % 2 != 0 and number >= 37:
            print("ваше место боковое нижнее")


def three():
    year = int(input("Введите год: "))

    if year % 4 == 0 and year % 100 != 0:
        print("Год " + str(year) + " високосный")
    else:
        print("Год " + str(year) + " не високосный")


def four():
    color1 = str(input("Выберите цвет (красный, синий, желтый): "))

    color2 = str(input("Выберите еще идин цвет: "))

    if ((color1 == "красный" or color1 == "Красный") and (color2 == "синий" or color2 == "Синий")) or (
            (color2 == "красный" or color2 == "Красный") and (color1 == "синий" or color1 == "Синий")):
        print("Фиолетовый")
    elif ((color1 == "красный" or color1 == "Красный") and (
            color2 == "желтый" or color2 == "Желтый" or color2 == "жёлтый" or color2 == "Жёлтый")) or (
            (color2 == "красный" or color2 == "Красный") and (
            color1 == "желтый" or color1 == "Желтый" or color1 == "жёлтый" or color1 == "Жёлтый")):
        print("Оражнеый")
    elif (color1 == "желтый" or color1 == "Желтый" or color1 == "жёлтый" or color1 == "Жёлтый") and (
            color2 == "синий" or color2 == "Синий") or (
            (color2 == "желтый" or color2 == "Желтый" or color2 == "жёлтый" or color2 == "Жёлтый") and (
            color1 == "синий" or color1 == "Синий")):
        print("Зеленый")
    else:
        print('Ошибка: введите название одного из трех основных цветов')


def five():
    n = int(input("Введите количество слов: "))

    result = ""

    for i in range(n):
        word = input(f"Введите слово №{i + 1}: ")
        result += word + " "

    print("Результат:", result.strip())
