import csv
import matplotlib.pyplot as plt

def read_data():
    allLines = {}
    with open("temps.csv") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            allLines[row[0]] = row[1]

    return allLines

def run():
    data = read_data()
    fig, axes = plt.subplots(2,1)
    indices = [1,2,3,4,5,6,7]
    axes[0].plot(indices,data["week1"])
    axes[0,1].plot(indices,data["week2"])
    plt.show()

run()