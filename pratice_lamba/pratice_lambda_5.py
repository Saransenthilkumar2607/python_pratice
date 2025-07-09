'''calling function in lambda function'''

def number(x, func):
    return func(x)

result = number(7, lambda x: x ** 2)
print(result)