import matplotlib.pyplot as plt


def read_data(details):
    result = []
    with open(details[1]) as file:
        for line in file:
            result.append(int(line))

    return result


def run():
    indexes = []
    data = read_data(("visualisation/subplots/temps/temps.txt", "temps.txt"))
    for i in range(len(data)):
        indexes.append(i + 1)
    fig, axes = plt.subplots(1, 2)
    axes[0].plot(indexes, data)
    axes[1].bar(indexes, data)
    plt.show()


run()
