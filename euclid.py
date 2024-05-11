from math import gcd

def gcd_classic(m, n):
    while m != n:
        if m > n:
            m = m - n
        else:
            n = n - m
    return m

def gcd_optimised(a, b):
    r = a % b
    while r:
        a = b
        b = r
        r = a % b
    return b

if __name__ == "__main__":
    gcd_classic(999_999, 2)
    print("=============")
    gcd_optimised(999_999, 2)