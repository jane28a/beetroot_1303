def min_sort(sequence):
    result = list()
    for counter in range(len(sequence)):
        min_element = min(sequence)
        index_of_min = sequence.index(min_element)
        sequence.pop(index_of_min)
        result.append(min_element)
        # result.append(sequence.pop(sequence.index(min(sequence))))
    return result

if __name__ == "__main__":
    to_sort = [15, 9, 8, 1, 4, 11, 7, 12, 13, 6, 5, 3, 16, 2, 10, 14]
    print(min_sort(to_sort))