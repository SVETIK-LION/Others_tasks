def avg_array(numbers: list):
    """
    Находит среднее арифметическое элементов массива
    :param numbers: Массив
    :return: Значение среднего арифметического
    """

    size_arr = len(numbers)
    sum_elem = 0

    for index in range(size_arr):
        sum_elem += numbers[index]
        index += 1

    avg = sum_elem / size_arr

    return avg


numbers_arr = [1, 2, 3, 4, 5]
print(avg_array(numbers_arr))
