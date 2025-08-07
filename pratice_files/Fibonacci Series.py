# def Fibonacci_Series(values):
#     a, b = 0, 1
#     while a <= values:
#         print(a, end=" ")
#         a, b = b, a + b

# Fibonacci_Series(2000)

def subset_sum(numbers, target):
    if target == 0:
        return True

    if not numbers:
        return False

    last = numbers[-1]
    remaining = numbers[:-1]

    return subset_sum(remaining, target) or subset_sum(remaining, target - last)

print(subset_sum([5, 10, 14, 68, 672], 100))
print(subset_sum([15, 16, 42, 65, 62], 100))