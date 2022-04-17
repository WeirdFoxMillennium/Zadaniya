def first_task(input_string=None):
    """
    1. Программа, рассчитывающая стоимость сообщения, где каждый символ стоит 40 копеек.
    :param input_string: входная строка
    :return: string
    """
    if not input_string:
        input_string = input("Введите строку для подсчета: ")

    s1 = (int(len(input_string) * 100) * 40) // 100
    rubles = s1 // 100
    cents = s1 % 100

    return f"{rubles} р. {cents} коп."


