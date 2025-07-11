import json 



# with open ("practice_json_values.json") as f :
#     details = json.load (f)

# for values in details["student"]:
#     print(values)



# student = {
#             "name": input("enter a name :"),
#             "number": int(input("enter a number :")),
#             "city": input("enter a city :"),
#             "city pincode": int(input("enter a city pincode :"))
# }
# file_location = r"C:\Users\saran\OneDrive\Desktop\saran\output.json"

# try: 
#     with open(file_location, "w") as file:
#         json.dump(student, file)
#         print(f"json file '{file_location}' was created")
# except FileExistsError :
#     print("this file is already exit")



# student = {
#             "name": input("enter a name :"),
#             "number": int(input("enter a number :")),
#             "city": input("enter a city :"),
#             "city pincode": int(input("enter a city pincode :"))
# }
# file_location = r"C:\Users\saran\OneDrive\Desktop\saran\practice_json_values.json"

# try: 
#     with open(file_location, "r") as file:
#         students_data =json.load(file)

#     students_data["student"].append(student)
    
#     with open(file_location,"w") as file:
#         json.dump(students_data, file, indent = 4)
#     print(f"json file '{file_location}' was added")

# except FileExistsError :
#     print("this file is already exists")

# print(students_data())





# file_location = r"C:\Users\saran\OneDrive\Desktop\saran\practice_json_values.json"

# try: 
#     with open(file_location, "r") as file:
#         students_data =json.load(file)
# except FileNotFoundError :
#     students_data = {"student": []}
    
# # user_number = []
# # for student in students_data["student"]:
# #     user_number.append(student["number"])
# old_number = [student["number"] for student in students_data["student"]]

# new_number = input("enter the mobile number :")

# # number_unique = True
# # for number in user_number:
# #     if user_number == number:
# #         numbreakber_unique = False
        
# if new_number in old_number:
#     print("this number is already used. please try an another number")
# else:
#     student = {
#         "name": input("enter a name :"),
#         "number": new_number,
#         "city": input("enter a city :"),
#         "city pincode": int(input("enter a city pincode :"))
#     }
        
#     students_data["student"].append(student)
    
#     with open(file_location,"w") as file:
#         json.dump(students_data, file, indent = 4)

#     print(f"json file '{file_location}' was added")






# file_location = r"C:\Users\saran\OneDrive\Desktop\saran\practice_json_values.json"

# with open(file_location, "r") as file:
#     data = json.load(file)

# select_name = input("enter student name for there details :")

# name_founded = False

# for student in data["student"]:
#     if student ["name"] == select_name:
#         print("name founded")
#         print("name :", student["name"])
#         print("number :", student["number"])
#         print("city :", student["city"])
#         print("city pincode :", student["city pincode"])

#         choose = input("if you want to update there name ? (yes / no):")
#         if choose == "yes":
#             student["name"] = input("enter an updated name :")
#             print("student name has been updated")
#         name_founded = True 
#         break
#     # else :

# if not name_founded:
#     print("no student with that name")

# with open(file_location, "w") as file:
#     json.dump(data, file, indent=4)
#     print("changes saved in the file")