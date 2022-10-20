def display_chars(file_name, number):
    line = ""
    with open(file_name) as file:
        for i in range(number):
            line += file.read(i)
    print(line)


def display_line(file_name):
    with open(file_name) as file:
        line = file.__next__()
        print(line)


def display_text(file_name):
    with open(file_name) as file:
        for line in file:
            print(line, end="")


def run():
    display_chars("library.txt", 5)
    display_line("library.txt")
    display_text("library.txt")


if __name__ == "__main__":
    run()
