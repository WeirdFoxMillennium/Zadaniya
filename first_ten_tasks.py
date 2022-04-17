from collections import Counter, defaultdict


def first_task(input_data=None):
    """
    1. Программа, рассчитывающая стоимость сообщения, где каждый символ стоит 40 копеек.
    :param input_data: входная информация
    :return:
    """

    s1 = (int(len(input_data) * 100) * 40) // 100
    rubles = s1 // 100
    cents = s1 % 100

    return f"{rubles} р. {cents} коп."


def second_task(first_string, second_string, third_string):
    """
    2. Программа упорядочивающая последовательность.
    На вход подаются три строки с ростом, на выход – три упорядоченные строки.
    :return:
    """
    input_data = [int(first_string), int(second_string), int(third_string)]
    input_data.sort(reverse=True)
    return str(input_data[0]), str(input_data[1]), str(input_data[2])


def third_task(input_data=None):
    """
    3. Напишите программу, которая проверяет, является ли введённое натуральное число степенью двойки.
    Если да, то выводится сама эта степень; если нет, выводится «НЕТ».
    :param input_data: входная информация
    :return:
    """
    degree = 0
    if input_data == 1:
        return 0
    while input_data > 1:
        input_data = input_data / 2
        degree += 1
        if input_data == 1:
            return degree
        elif input_data < 1:
            return 'НЕТ'


def fourth_task():
    pass


def fifth_task(n: int, w: int, h: int):
    """
    5. Функция, которая возвращает количество полных стен, которые я могу покрасить,
    прежде чем мне нужно будет отправиться в магазины, чтобы купить еще.
    :param n: количество квадратных метров
    :param w: ширина одной стены в метрах
    :param h: высота одной стены в метраж
    :return:
    """
    wall = int(n / (w * h))
    return wall


def sixth_task(prob, prize, pay):
    """
    6.	Функция, которая принимает три аргумента prob, prize, pay и возвращает true,
     если prob * prize > pay; в противном случае возвращает false.
    :param prob:
    :param prize:
    :param pay:
    :return:
    """
    if prob * prize > pay:
        return True
    else:
        return False


def seventh_task():
    pass


def eighth_task(first_num: int, second_num: int, third_num: int):
    """
    8. Функция, которая принимает три целочисленных аргумента
    и возвращает количество целых чисел, имеющих одинаковое значение.
    :param first_num: первое число
    :param second_num:  второе число
    :param third_num: третье число
    :return: количество одинаковых значений
    """

    list_nums = [first_num, second_num, third_num]

    counter = defaultdict(int)
    for num in list_nums:
        counter[num] += 1
    if len([True for num in counter.values() if num == 1]) == len((counter.values())):
        return 0

    return max(counter.values())


def ninth_task(input_data):
    """
    9.	Функция, которая находит слово "бомба" в данной строке. Ответьте "ПРИГНИСЬ!",
    если найдешь, в противном случае: "Расслабься, бомбы нет".
    :param input_data:
    :return:
    """
    if 'бомба' in input_data.lower():
        return 'ПРИГНИСЬ!'
    return "Расслабься, бомбы нет."


def tenth_task(input_data):
    """
    10. Функция обратного обращения строки.
    Все буквы в нижнем регистре должны быть прописными, и наоборот.
    :param input_data:
    :return:
    """
    char_list = [c.upper() if c.islower() else c.lower() for c in input_data]
    return "".join(char_list)
