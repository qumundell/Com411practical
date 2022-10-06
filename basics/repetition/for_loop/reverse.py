characters = input("What phrase do you see?\n")
print("\nReversing...\n")
reverseArray = []
for char in range(0, len(characters), 1):
    reverseArray.append(f"{characters[char]}")
print("The phrase is: ", end="")
for char in range(len(characters)-1, -1, -1):
    print(reverseArray[char], end="")
