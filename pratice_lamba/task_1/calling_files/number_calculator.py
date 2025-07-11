def collect_numbers():
    while True:
        try:
            count = int(input("How many numbers do you want to calculate: "))
            if count < 1:
                print("Please enter at least 1 number.")
                continue
            break
        except ValueError:
            print("Invalid input, please enter a whole number.")
    number = []

    for i in range(count):
        while True:
            num_input = input(f"enter number {i + 1} :")
            try:   
                num = float(num_input)
                number.append(num)
                break
            except ValueError:
                print ("invalid input, please enter an numberical number")
    return number