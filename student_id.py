import json 


# file_location = r"C:\Users\saran\OneDrive\Desktop\saran\student_id.json"

# try: 
#     with open(file_location, "r") as file:
#             student_data = json.load(file)


# except FileExistsError :
#     print("this file is already exit")


# reg_roll_number = [student["roll number"] for student in student_data["student"]]

# new_roll = input("enter the roll number :")

# if new_roll in reg_roll_number:
#     print("this number is already used. please try an another number")

# else:
    # student = {
    #     "name": input("enter a name :"),
    #     "roll number": new_roll,
    #     "number": int(input("enter a number :")),
    #     "city": input("enter a city :"),
    #     "city pincode": int(input("enter a city pincode :"))
    # }
        
#     student_data["student"].append(student)
    
#     with open(file_location,"w") as file:
#         json.dump(student_data, file, indent = 4)

#     print(f"json file '{file_location}' was added")







# file_location = r"C:\Users\saran\OneDrive\Desktop\saran\student_id.json"

# with open(file_location, "r") as file:
#     data = json.load(file)

# select_roll_number = input("enter student roll number for there details :")

# roll_number_founded = False

# for student in data["student"]:
#     if student ["roll number"] == select_roll_number:
#         print("roll number was founded")
#         print("name :", student["name"])
#         print("roll number :", student["roll number"])
#         print("number :", student["number"])
#         print("city :", student["city"])
#         print("city pincode :", student["city pincode"])

#         choose = input("if you want to update there rollnumber? (yes / no):")
#         if choose == "yes":
#             student["roll number"] = input("enter an updated roll number :")
#             print("student roll number has been updated")
#         roll_number_founded = True 
#         break

# if not roll_number_founded:
#     print("no student with that roll number")

# with open(file_location, "w") as file:
#     json.dump(data, file, indent=4)

#     print("changes saved in the file")






# file_location = r"C:\Users\saran\OneDrive\Desktop\saran\student_id.json"

# with open(file_location, "r") as file:
#     data = json.load(file)

# select_roll_number = input("enter student roll number for there details :")

# roll_number_founded = False

# for student in data["student"]:
#     if student ["roll number"] == select_roll_number:
#         print("roll number was founded")
#         print("name :", student["name"])
#         print("roll number :", student["roll number"])
#         print("number :", student["number"])
#         print("city :", student["city"])
#         print("city pincode :", student["city pincode"])

#         for student in data ["student"]:
#             choose = input("if you want to do anything like (update / add / details / list ):")
        
#             if choose == "update":
#                 student["city"] = input("enter an updated city :")
#                 print("student city has been updated")

#             elif choose == "add":
#                 student["age"] = input("enter an student age :")
#                 print("student age has been added")
        
#             elif choose == "details":
#                 student["details"] = select_roll_number
#                 print("name :", student["name"])
#                 print("roll number :", student["roll number"])
#                 print("number :", student["number"])
#                 print("city :", student["city"])
#                 print("city pincode :", student["city pincode"])

#             elif choose == "list":
#                 print(student)
                
#         city_founded = True 
#         break
        
        
#         # else choose == "end":
#         #         print("the student details were ended")

#         # city_founded = True 
#         # break

# if not roll_number_founded:
#     print("no student with that roll number")

# with open(file_location, "w") as file:
#     json.dump(data, file, indent=4)
    
#     print("changes saved in the file")




file_location = r"C:\Users\saran\OneDrive\Desktop\saran\student_id.json"

with open(file_location, "r") as file:
    data = json.load(file)

if "last_id" not in data:
    data ["last_id"] = 0
    for i , student in enumerate (data["student"], start = 1):
        student["unique id"] = i
        data["last_id"] = i

choose = input("if you want to do anything like (update / add / details / list ):")
    
if choose == "update":
    rollnumber =input("enter a roll number :")
    founded = False
    
    for student in data ["student"]:
        if student["roll number"] == rollnumber:
            student["name"] = input("enter an updated name :")
            student["number"] = input("enter an updated number :")
            student["city pincode"] = input("enter an updated city pincode :")
            student["city"] = input("enter an updated city :")
            print("student city has been updated")
            founded = True
            print("stduent data updated")
            break

        if not founded :
              print("student in this roll number us not founded")

elif choose == "add":
    data["last_id"] += 1
    new_student = {
        #  "unique id": data["last_id"],
        "name": input("enter a name :"),
        "roll number": input("enter a roll number :"),
        "number": int(input("enter a number :")),
        "city": input("enter a city :"),
        "city pincode": int(input("enter a city pincode :")),
        "unique id": data["l" \
        "ast_id"]
    }
    data ["student"].append(new_student)
    print("new student data us added")

elif choose == "details":
    rollnumber =input("enter a roll number :")
    founded = False
    
    for student in data ["student"]:
        if student["roll number"] == rollnumber:
            print("name :", student["name"])
            print("roll number :", student["roll number"])
            print("number :", student["number"])
            print("city :", student["city"])
            print("city pincode :", student["city pincode"])
            founded = True
            print("stduent data details as been showed")

    if not founded :
              print("student in this roll number us not founded")

elif choose == "list":
    for student in data ["student"]:
        print(student)

else:
    print(choose = input("if you want to do anything like (update / add / details / list ):"))

with open(file_location, "w") as file:
    json.dump(data, file, indent=4)
    
    print("changes saved in the file")




