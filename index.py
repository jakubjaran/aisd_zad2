import time
import pandas
import sys

from quick_sort import quick_sort
from list_generator import list_generator


def test_qs(list, pivot):
    list_copy = list[:]
    start = time.time()
    quick_sort(list_copy, pivot)
    end = time.time()
    elapsed = end - start
    return elapsed


def main():
    sys.setrecursionlimit(999999999)

    print("List length:")
    list_length = int(input())

    print("Step:")
    step = int(input())

    print("Tests:")
    tests = int(input())

    writer = pandas.ExcelWriter(f'out/qs_{list_length}_{step}_{tests}.xlsx')

    for i in range(0, 15 * step, step):
        print(f'List length: {list_length + i}')
        pivot_right = []
        pivot_middle = []
        pivot_random = []
        for j in range(tests):
            print(f'Test {j+1}')
            list = list_generator(list_length + i)
            pivot_right.append(test_qs(list, 'right'))
            pivot_middle.append(test_qs(list, 'middle'))
            pivot_random.append(test_qs(list, 'random'))
        data = pandas.DataFrame({
            'right': pivot_right,
            'middle': pivot_middle,
            'random': pivot_random
        })
        data.to_excel(writer, sheet_name=f'{list_length+i}', index=False)
        data = None

    writer.save()


main()