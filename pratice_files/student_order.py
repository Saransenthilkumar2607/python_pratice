# 1 . student1 : saran
# 2 . student2 : saran2

import json 


file_location = r"C:\Users\saran\OneDrive\Desktop\saran\key_values.json"
file_location2 = r"C:\Users\saran\OneDrive\Desktop\saran\key_values_2.json"

with open(file_location, "r") as file:
    
    data = json.load(file)

key_list = list(data.keys())

# for key in key_list:
#     print(f"{s_no}. {key} : {data[key]}")
#     s_no += 1
[print(f"{i+1}. {key} : {data[key]}")for i, key in enumerate (key_list)]

total_students = len(data)
User_order = []

print(f"enter a new student order of {total_students} one by one ")

while len(User_order) < total_students :
    User_input = input("enter number : ")

    try :
        number = int(User_input)

        if number <1 or number > total_students :
            print(f"enter the number in the range of 1 - {total_students}....?")
            continue

        if number in User_order:
            print("this number is already entered")
            continue

        User_order.append(number)

    except ValueError:
        print("*WRONG ENTRY *enter an correct value (eg: 1,2,3...)")
    
print("your enter order : ", User_order)

new_list = {}
for num in User_order:
    key = f"student{num}"
    if key in data:
        new_list[key] = data[key]
    else:
        print(f"the input value form user{num}is not in json")
print(new_list)

with open(file_location2, "w") as file:
    json.dump(new_list, file, indent=4)
    
    print("changes of student data saved in the file")

