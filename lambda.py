
# list(map(lambda x: print(x), range(1, 101)))

# number = input("Enter numbers separated by commas(,): ")  
# number_list = map(int, number.split(','))             
# squar_number = set(map(lambda x: x**2, number_list))  
# print(squar_number)


# student_order = [("saran" , 90), ("arun", 85), ("raj", 95), ("kamal", 60)]

# sorted_order_student = sorted(student_order, key = lambda x : x [1],reverse= False)
# print(sorted_order_student)


# student_order = [("saran" , 90), ("arun", 85), ("raj", 95), ("kamal", 60)]

# sorted_order_student = sorted(student_order, key = lambda x : x [1],reverse= True)
# print(sorted_order_student)


# def number(x, func):
#     return func(x)

# result = number(7, lambda x: x ** 2)
# print(result)

bigger_number = lambda a, b : a if a > b else b
print("bigger number is : ", bigger_number(50, 75))