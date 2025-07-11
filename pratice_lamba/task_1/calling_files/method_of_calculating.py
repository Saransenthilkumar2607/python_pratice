def addition (numbers):
    return sum(numbers)

def subtract (numbers):
    result = numbers[0]
    for num in numbers [1 :]:
        result -= num
    return result

def multiply (numbers):
    result = numbers [0]
    for num in numbers[1:]:
        result *= num
    return result


def division (numbers):
    result = numbers[0]
    for num in numbers[1 :]:
        if num == 0 :
            return "any number division by 0 is zero"
        result /= num
    return result

