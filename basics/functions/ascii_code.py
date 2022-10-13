print("Program started!")
character = input("Please enter a standard character: ")
if len(character) == 1:
    print(f"The ASCII code for {character} is: {ord(character)}")
else:
    print("The input you gave has multiple characters")
print("Program Ended!")
