# quicksort.py

def quicksort(arr, compare_func, low=0, high=None):
    """
    Реализация быстрой сортировки (Хоара) с пользовательской функцией сравнения.
    arr — список для сортировки (изменяется на месте).
    compare_func(a, b) — должна вернуть True, если a должен быть ДО b.
    """
    if high is None:
        high = len(arr) - 1
    if low < high:
        pi = partition(arr, compare_func, low, high)
        quicksort(arr, compare_func, low, pi - 1)
        quicksort(arr, compare_func, pi + 1, high)


def partition(arr, compare_func, low, high):
    """Вспомогательная функция для Quicksort."""
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if compare_func(arr[j], pivot):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
