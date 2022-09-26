def sum_between_min_max(lst: list):
    ind_min_elem = lst.index(min(lst))
    ind_max_elem = lst.index(max(lst))

    if ind_min_elem < ind_max_elem:
        result = sum(lst[ind_min_elem + 1:ind_max_elem])
    else:
        result = sum(lst[ind_max_elem + 1:ind_min_elem])

    return f'{result}'


list_1 = [4, 1, 10, 5, 6, 0, 4]
list_2 = [4, 1, 0, 5, 6, 10, 4]
print(sum_between_min_max(list_1))
print(sum_between_min_max(list_2))
