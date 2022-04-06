def task(num: int) -> bool:  # TODO добавить аннотацию типов
    list_ = [int(d) for d in str(abs(num))]
    if sum(list_) > 9:
        return True
    else:
        return False



if __name__ == "__main__":
    print(task(12))
    print(task(555))
    print(task(-12))
    print(task(-149))
