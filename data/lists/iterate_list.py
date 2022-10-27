def directions():
    l_directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return l_directions


def menu():
    print("Please select a direction: ")
    directions_l = directions()
    for i in range(len(directions_l)):
        print(f"{i}: {directions_l[i]}")


def run():
    menu()


run()
