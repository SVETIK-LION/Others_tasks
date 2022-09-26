def index_max_min_elem(numbers: list):
    max_elem = max(numbers)
    min_elem = min(numbers)
    index_max_elem = numbers.index(max_elem)
    index_min_elem = numbers.index(min_elem)

    return f'Индекс минимального элемента массива: {index_min_elem}\n' \
           f'Индекс максимального элемента массива: {index_max_elem}'


my_list = [1, 6, 25, 0, 4]
print(index_max_min_elem(my_list))
