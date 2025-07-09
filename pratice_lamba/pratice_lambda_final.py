def my_sorted (number):
    n = len (number)
    for i in range (n):
        for j in range (0, n-i-1):
            if student[j] > student[j+1]:
                student[j], student[j+1] = student[j+1], student[j]
    return number

student = [("ajay", 80, 80, 50), ("arun", 80, 87, 50), ("viswa", 80, 70, 37), ("abi", 60, 50, 48)]
print("mark and name of the student :", student)
total_marks = list(map(lambda x : (x[0], x[1] + x[2] + x[3]), student))

print("total marks of the student :", total_marks)

top_marks = my_sorted(total_marks)

rank = 1
old_marks = None
count = 0
older_marks = 1

for name, total in top_marks:
    if total != old_marks :
        older_marks = rank 
    print(f"rank {older_marks}:{name},{total}")
     
    old_marks = total
    rank += 1
    count += 1
    if count == 4:
        break