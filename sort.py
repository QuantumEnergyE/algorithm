def quick_sort(data):
    pass


def bubble_sort(data):
    is_sorted = False
    length = len(data) - 1
    while not is_sorted:
        is_sorted = True
        for i in range(length):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                is_sorted = False
        length -= 1
