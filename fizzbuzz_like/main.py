def main():
    error_message = "You must enter integer greater than 0"

    input_number = input("Enter integer greater than 0: ")
    if not (input_number.isdigit() and int(input_number) > 0):
        print(error_message)
        return

    num = int(input_number)

    conditions = {
        lambda a: a % 5 == 0 and a % 3 == 0: "Testing",
        lambda a: a % 5 == 0: "Agile",
        lambda a: a % 3 == 0: "Software",
    }

    for i in range(num, 0, -1):
        for condition, message in conditions.items():
            if condition(i):
                print(message)
                break
        else:
            print(i)


if __name__ == "__main__":
    main()
