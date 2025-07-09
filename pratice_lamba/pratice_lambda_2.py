'''squar numbers'''


number = input("Enter numbers separated by commas(,): ")  
number_list = map(int, number.split(','))             
squar_number = set(map(lambda x: x**2, number_list))  
print(squar_number)

