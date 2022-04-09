from random import randint


def partition(array, low, high, pivot):
    if pivot == 'right':
        pv = len(array) - 1
    if pivot == 'middle':
        pv = int(len(array) / 2)
    if pivot == 'random':
        pv = randint(0, len(array) - 1)
    i = low - 1
    for j in range(low, high):
        if array[j] <= array[pv]:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quick_sort_rec(array, low, high, pivot):
    if low < high:
        pi = partition(array, low, high, pivot)
        quick_sort_rec(array, low, pi - 1, pivot)
        quick_sort_rec(array, pi + 1, high, pivot)


def quick_sort(array, pivot):
    quick_sort_rec(array, 1, len(array) - 1, pivot)
