# O(1)
def return_first(iterable):
    return iterable[0]

# O(log(n))
def binary_search(iterable):
    pass

# O(n**k, k<1)
def tree_search(tree):
    pass

# O(n)
def double_value(iterable):
    result = list()
    for element in interable:
        result.append(element * 2)
    return result
    # return [element *2 for element in iterable]

# O(n*log(n))
def find_max():
    the_list = [[1, 2, 3], [9, 6, 4, 45, 7], [4, 7, 8, 11]]
    tmp_max = 0
    for sublist in the_list:
        for element in sublist:
            if element > tmp_max:
                tmp_max = element

    sublist_max = []
    for sublist in the_list:
        sublist_max.append(max(sublist))
    return max(sublist_max)

# O(2 * n) => O(n)
def print_double(iterable):
    result = list()
    for element in interable:
        result.append(element * 2)
    for item in result:
        print(item)

# O(n**2)
def my_sort(iterable):
    for element in iterable:
        for other_element in iterable:
            if element < other_element:
                # swap elements

# O(e**n)
