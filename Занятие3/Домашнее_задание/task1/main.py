def input_numbers():
    number_list = []

    while True:
        input_num = int(input("Введите новое число: "))
        if input_num < 0:
            number_list.append(input_num)
            break
        if 3 <= input_num <= 13:
            number_list.append(input_num)


    return number_list

if __name__ == "__main__":
    numbers = input_numbers()
    print(numbers)
