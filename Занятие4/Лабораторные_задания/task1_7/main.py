from statistics import mean
if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 4, -3, -6, 8, 6, 9]
    avg_list = mean(list_)
    new_list = [float(list_[i]) - avg_list for i in range(len(list_))]  # TODO Заполните список с помощью list comprehension

    print(new_list)
