list1 = [6, 10, 15]
list2 =[56, 5, 70]

result = list(map(lambda x : x [0] * int(x[1]), zip(list1, list2)))
print(f"multiplying corresponding : {result}")



