names = []
exam1 = []
exam2 = []

def load_data(path):
    with open(path) as file:
        for line in file.readlines():
            line = line.strip().split(",")
            names.append(line[0])
            exam1.append(int(line[1]))
            exam2.append(int(line[2]))

load_data("English.txt")
print(f"Successfully loaded {len(names)} records.")