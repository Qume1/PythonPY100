def is_palindrome_number(num: int) -> bool:
    if num < 0:
        return False
    list_ = [int(d) for d in str(abs(num))]

    reverse_list = list(reversed(list_))

    return True if list_ == reverse_list else False  # TODO проверить является ли число палиндром


if __name__ == "__main__":
    print(is_palindrome_number(1234))
    print(is_palindrome_number(1234321))
