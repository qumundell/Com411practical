distance = int(input("How far are we from the cave?\n"))
print()
for steps in range(distance, 0, -1):
    print(f"{steps} steps remaining")

print("\nWe have reached the cave!")