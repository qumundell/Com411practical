brightness = int(input("What level of brightness is required? \n"))
done = False
while done is False:
    brightness = int(input("What level of brightness is required? (even number) \n"))
    if brightness % 2 == 0:
        done = True
for bLevel in range(0, brightness - 1, 2):
    stars = ""
    for _ in range(0, bLevel + 2):
        stars += "*"

    print("\n\n")
    print("Beep's brightness level: " + stars)
    print("Bop's brightness level: " + stars)

print("Adjustments complete!")
