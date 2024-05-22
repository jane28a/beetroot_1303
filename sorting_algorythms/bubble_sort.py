def bubble_sort(sequence):
    for counter in range(len(sequence)):
        for index in range(len(sequence) - counter - 1):
            if sequence[index] > sequence[index+1]:
                sequence[index], sequence[index+1] = sequence[index+1], sequence[index]
        print(sequence)
    return sequence

if __name__ == "__main__":
    to_sort = [15, 9, 8, 1, 4, 11, 7, 12, 13, 6, 5, 3, 16, 2, 10, 14]
    print(bubble_sort(to_sort))