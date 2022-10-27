def directions():
    l_directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return l_directions


def menu():
    print("Please select a direction: ")
    directions_l = directions()
    for i in range(len(directions_l)):
        print(f"{i}: {directions_l[i]}")
    u_input = int(input())
    return directions_l[u_input]


def run():
    route = []
    print("Working out escape route...")
    for _ in range(5):
        route.append(menu())
    print(f"Escape route: {route}")


run()
