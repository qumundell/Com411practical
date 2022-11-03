def observed():
    observations = []
    for _ in range(5):
        observations.append(input("Input your observations: "))

    return observations


def remove_observations(observations):
    done = input("Do you wish to remove observations? (y/n) ")
    while done == "n":
        delObs = input("What observation do you wish to remove? ")
        observations.remove(delObs)
        print("Done!")
        done = input("Do you wish to remove more observations? (y/n) ")


def run():
    obsList = observed()
    remove_observations(obsList)
    obsAsSet = set()
    for i in range(len(obsList)):
        obsAsSet.add((obsList[i], obsList.count(obsList[i])))

    print(obsAsSet)


run()