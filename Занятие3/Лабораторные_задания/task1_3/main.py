def get_list_number_divisors(number):
    list_ = []
    divider = 1
    while True:
        if number == divider:
            list_.append(divider)
            break
        if number % divider == 0:
            list_.append(divider)

        divider += 1

    return list_

if __name__ == "__main__":
    print(get_list_number_divisors(2 ** 16))
