def observed():
    observations = []
    for _ in range(7):
        observations.append(input("Please input your observations: "))
    return observations


def run():
    print("Counting observations...")
    obsList = observed()
    obsAsSet = set()
    for i in range(len(obsList)):
        obsAsSet.add((obsList[i], obsList.count(obsList[i])))

    print(obsAsSet)


run()
