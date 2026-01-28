import random

def bubbleSort(items: list):
    swaps = 0
    comparisons = 0
    n = len(items)

    for i in range(n - 1):
        for j in range(n - 1):
            comparisons += 1
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                swaps += 1
                comparisons += 1

    return items, swaps, comparisons


def insertionSort(items: list):
    swaps = 0
    comparisons = 0

    for i in range(1, len(items)):
        key = items[i]
        j = i - 1

        while j >= 0 and items[j] > key:
            comparisons += 1
            items[j + 1] = items[j]
            swaps += 1
            j -= 1

        if j >= 0:
            comparisons += 1

        items[j + 1] = key

    return items, swaps, comparisons


def selectionSort(items: list):
    swaps = 0
    comparisons = 0
    n = len(items)

    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if items[j] < items[min_idx]:
                min_idx = j

        items[i], items[min_idx] = items[min_idx], items[i]
        swaps += 1

    return items, swaps, comparisons
