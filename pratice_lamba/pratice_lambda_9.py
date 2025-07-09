list1 = ["apple", "banana ", "grapes "]
list2 =["1", "5", "7"]

result = list(map(lambda x : x [0] * int(x[1]), zip(list1, list2)))
print(f"multiplying corresponding : {result}")

