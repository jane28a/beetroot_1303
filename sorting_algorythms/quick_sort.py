def quick_sort(sequence):
    if len(sequence) <= 1:
        return sequence

    pivot = sequence[0]
    left = [element for element in sequence[1:] if element < pivot]
    right = [element for element in sequence[1:] if element >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == "__main__":
    to_sort = [15, 9, 8, 1, 4, 11, 7, 12, 13, 6, 5, 3, 16, 2, 10, 14]
    print(quick_sort(to_sort))