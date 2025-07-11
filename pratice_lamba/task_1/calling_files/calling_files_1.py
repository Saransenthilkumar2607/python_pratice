def addition (numbers):
    return sum(numbers)

def subtract (numbers):
    result = numbers[0]
    for num in numbers [1 :]:
        result -= num
    return result


def multiply (numbers):
    result = numbers [0]
    for num in numbers[1:]:
        result *= num
    return result

def division (numbers):
    result = numbers[0]
    for num in numbers[1 :]:
        if num == 0 :
            return "any number division by 0 is zero"
        result /= num
    return result
    
def calculatore ():
    print("select the method of calculating with numbers :\n1. addition\n2. subtract\n3. multiply\n4. division")

    choice = input("enter choice (1/2/3/4): ")

    if choice not in ("1", "2", "3","4"): 
        print ("error only enter a value of the number to calculate")
        return


    count = int(input("how many numbers to you want to calculate :"))
    number = []

    for i in range (count):
        while True:
            num_input = input(f"enter number {i + 1} :")
            try:
                num = float(num_input)
                number.append(num)
                break
            except ValueError:
                print ("invalid input, please enter an numberical number")

    if choice == "1":
        print ("addition :", addition(number))
    
    if choice == "2":
        print ("subtract :", subtract(number))
    
    if choice == "3":
        print ("multiply :", multiply(number))
    
    if choice == "4":
        print ("division :", division(number) )





