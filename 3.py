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

def show_results(arr1, arr2, exam_name):
    print(f"{exam_name}:")
    print("-" * 10)
    for name, score in zip(arr1, arr2):
        if score != -1:
            print(f"{name:15}{score}")

def show_menu(names, exam1, exam2):
    while True:
        print("1. Show Results of Each Exam ")
        print("2. Missing Students ")
        print("3. Top Marks ")
        print("4. -")
        print("5. -")
        print("6. Exit ")
        choice = input("Enter your choice: ")
        try:
            choice = int(choice)
        except ValueError:
            print("Invalid input, please enter a number.\n")
            continue

        if choice == 1:
            show_results(names, exam1, "Exam 1")
            print()
            show_results(names, exam2, "Exam 2")
            print()
        elif choice == 6:
            break
        else:
            print("Function not implemented yet.\n")

show_menu(names, exam1, exam2)