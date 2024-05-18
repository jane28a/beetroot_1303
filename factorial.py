def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

def factorial_rec(n):
    if n == 1:
        return 1
    return n * factorial_rec(n-1)

if __name__ == "__main__":
    # print(factorial(2000))

    print(factorial_rec(5))