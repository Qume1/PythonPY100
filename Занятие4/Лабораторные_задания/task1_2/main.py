def task(n: int, m: int) -> list:  # TODO указать аннотацию типов
    return [x ** 2 for x in range(n, m+1) if x % 2 != 0] # TODO с помощью list comprehension отфильтровать знаечения


if __name__ == "__main__":
    number_n = 5
    number_m = 37
    print(task(5, 37))
