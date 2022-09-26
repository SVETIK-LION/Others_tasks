def avg_list(lst: list):
    sum_list = sum(lst)
    length_list = len(lst)
    avg_elems = sum_list / length_list

    return avg_elems


my_list = [1, 2, 3, 4, 5]
print(avg_list(my_list))
