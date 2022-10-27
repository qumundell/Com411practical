def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    return likelihoods[-1]


def run():
    value = likelihood()
    print(f"Minimum likelihood of falling: {value}%")


run()
