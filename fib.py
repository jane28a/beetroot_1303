def problem_2():
    a, b = 1, 2
    even_sum = 0

    def get_next_value():
        nonlocal a, b
        a, b = b, a + b

    def accumulate_sum():
        nonlocal b, even_sum
        if not b % 2:
            even_sum += b

    while b < 4_000_000:
        accumulate_sum()
        get_next_value()
    print(even_sum)

problem_2()


def list_map(func, sequence):
    from collections.abc import Iterable
    if not isinstance(sequence, Iterable):
        sequence = list(sequence)
    return [func(element) for element in sequence]

