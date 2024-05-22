def choice_sort(sequence):
    
    def get_max_index():
        max_index = 0
        for index in range(right_bound + 1):
            if sequence[max_index] < sequence[index]:
                max_index = index
        return max_index

    right_bound = len(sequence) - 1
    while right_bound > 1:
        max_index = get_max_index()
        sequence[right_bound], sequence[max_index] = sequence[max_index], sequence[right_bound]
        right_bound -= 1
        print(sequence)
    return sequence

if __name__ == "__main__":
    to_sort = [15, 9, 8, 1, 4, 11, 7, 12, 13, 6, 5, 3, 16, 2, 10, 14]
    print(choice_sort(to_sort))