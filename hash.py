NUM_BUCKETS = 4

def bin_hash(value):
    return value % NUM_BUCKETS

if __name__ == "__main__":
    hash_table = [[], [], [], []]
    sequence = [15, 9, 8, 1, 4, 11, 7, 12, 13, 6, 5, 3, 16, 2, 10, 14]
    for element in sequence:
        hash_table[bin_hash(element)].append(element)
    print(hash_table)
    to_find = 17
    for element in hash_table[bin_hash(to_find)]:
        print(element)
        if element == to_find:
            print("Found")
            break
    else:
        print("Not found")
