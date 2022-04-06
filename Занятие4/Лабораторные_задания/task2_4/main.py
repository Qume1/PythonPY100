def digit_sum(num: int) -> bool:
    list_ = [int(d) for d in str(abs(num))]
    return True if len(str(num)) == 4 and sum(list_) % 7 == 0 else False# TODO не забыть проерить, что число дожно быть четырехзначное

    ...  # TODO проверить кратность суммы цифр


if __name__ == "__main__":
    print(digit_sum(1234))
    print(digit_sum(7777))
