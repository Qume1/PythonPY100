def factorial(n):
    a = 1
    prov = n
    while a < prov:
        n *= a
        a += 1

    return n


if __name__ == "__main__":
    res = factorial(int(input()))
    print(res)
