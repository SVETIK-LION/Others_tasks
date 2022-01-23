#7.1.a
from typing import List, Any


def mass(n):
    mass = [number for number in range(1, n + 1)]
    print(mass)

mass(6)

#7.1.b
def sum_digit(mass):
    sum_d = sum(mass)
    print(sum_d)

sum_digit([4, 4, 4, 4])

#7.1.c
def max_digit(mass_int):
    largest = max(mass_int)
    print(largest)

max_digit([1, 2, 3, 155, 4, 5])

#7.1.d
def min_digit(mass_int):
    smallest = min(mass_int)
    print(smallest)

min_digit([1, -44, 2, 3, 155, 4, 5])

#7.1.f
def even_digit(mass_int):
    even: list[Any] = [digit for digit in mass_int if digit % 2 == 0]
    print(*even)

even_digit([1, -44, 2, 3, 155, 4, 5])


