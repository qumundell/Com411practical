characters = input("What strange markings do you see?\n")
print("\nIdentifying...\n")
for char in range(0, len(characters), 1):
    print(f"Index {char}: {characters[char]}")
print("\nDone!")
