import imp
from random import randint


def list_generator(length):
    half_length = int(length / 2)

    left_list = [None] * half_length

    for i in range(half_length):
        left_list[i] = randint(0, 100)

    left_list.sort()

    right_list = left_list[:]
    right_list.sort(reverse=True)

    list = left_list + right_list

    return list