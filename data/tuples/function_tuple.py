def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    big_val = 0
    low_val = 100
    for i in range(len(likelihoods)):
        if big_val < likelihoods[i]:
            big_val = likelihoods[i]
        if low_val > likelihoods[i]:
            low_val = likelihoods[i]

    return low_val, big_val


def run():
    value = likelihood()
    print(f"Minimum likelihood of falling: {value[0]}%")
    print(f"Maximum likelihood of falling: {value[1]}%")


run()
