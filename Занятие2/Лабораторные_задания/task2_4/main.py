if __name__ == "__main__":
    phrase = "Hello,world"
    initial_offset = 5  # TODO чему равно начальное смещение?""
    for index, value in enumerate(phrase, start=initial_offset):
        print(" " * index, value)
# TODO как использовать начальное смещение в команде enumerate?
