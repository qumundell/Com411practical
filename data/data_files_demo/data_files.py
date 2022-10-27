import csv
import json

# with open("demo.txt", 'ra') as file:
#     for line in file:
#         print(line, end=" ")

with open("demo.csv") as file:
    csv_reader = csv.reader(file)
    heading = next(csv_reader)
    print(heading)
    for row in csv_reader:
        print(row)
        print(f"The leader of {row[1]} is {row[2]}")

# with open("demo.json") as file:
#     data = json.load(file)
#     for item in data:
#         print(f"The leader of {item['name']} is {item['leader']}, {item['code']}")
