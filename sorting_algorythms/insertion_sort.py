def insertion_sort(sequence):
    for index in range(1, len(sequence)):
        position = index - 1
        value = sequence[index]
        while position >= 0 and sequence[position] > value:
            sequence[position + 1] = sequence[position]
            position -= 1
        sequence[position + 1] = value
        print(sequence)
    return sequence

if __name__ == "__main__":
    to_sort = [15, 9, 8, 1, 4, 11, 7, 12, 13, 6, 5, 3, 16, 2, 10, 14]
    print(insertion_sort(to_sort))