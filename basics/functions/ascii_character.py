print("Program Started!")
done = False
while done is False:
    try:
        u_input = input("Please enter an ASCII code:")
        u_int = int(u_input)
        if u_int in range(32, 126):
            done = True
    except TypeError:
        print("Number was not within a suitable range (32-126)")
print(f"The character represented by the ASCII code {u_input} is \"{chr(u_int)}\"")
print("Program Ended!")
