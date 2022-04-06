def check(n: int, m: int) -> str:
    if n > m:
        return "Четных больше"
    elif n < m:  # TODO распечатать каких чисел больше. Учтите, что длины могу быть равны
        return "Нечетных больше"
    else:
        return "Кол-во чисел равно"

if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    even_list_ = [i for i in list_ if i % 2 == 0]  # TODO получить два списка четных и нечетных чисел
    not_even_list_ = [i for i in list_ if i % 2 != 0]

    len_even_list_ = len(even_list_)  # TODO найти длины этих списков
    len_not_even_list_ = len(not_even_list_)

    check(len_even_list_, len_not_even_list_)
