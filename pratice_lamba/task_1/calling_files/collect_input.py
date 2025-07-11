import method_of_calculating
import number_calculator

def number_input():
    print("select the method of calculating with numbers :\n1. addition\n2. subtract\n3. multiply\n4. division")

    choice = input("enter choice (1/2/3/4): ")

    if choice not in ("1", "2", "3","4"): 
        print ("error only enter a value of the number to calculate")
        return None
    return choice

choice = number_input()
if choice:
    numbers = number_calculator.collect_numbers()

    if choice == "1":
        print ("addition :", method_of_calculating.addition(numbers))
    
    elif choice == "2":
        print ("subtract :", method_of_calculating.subtract(numbers))
    
    elif choice == "3":
        print ("multiply :", method_of_calculating.multiply(numbers))
    
    elif choice == "4":
        print ("division :", method_of_calculating.division(numbers) )

