def movements():
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path


def run():
    print("Moving...")
    result = movements()
    for i in range(0, len(result), 2):
        print(f"{result[i]} for {result[i + 1]} steps")


run()
