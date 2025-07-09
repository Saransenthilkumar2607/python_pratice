"""descending to ascending order"""


student_order = [("saran" , 90), ("arun", 85), ("raj", 95), ("kamal", 60)]

sorted_order_student = sorted(student_order, key = lambda x : x [1],reverse= False)
print(sorted_order_student)
