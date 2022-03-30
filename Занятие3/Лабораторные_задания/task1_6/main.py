def sum_(salary, spend, months=10, inf=0.03):
    help_sum = 0
    for i in range(months):
        help_sum += spend - salary
        spend *= 1 + inf



    return help_sum

if __name__ == "__main__":

    print(sum_(5000, 6000))  # TODO вызвать функцию и проверить работоспособность
