def fibonacci_numbers(nums):
    x, y = 1, 1

    for _ in range(nums):
        yield x
        x, y = y, x + y

def square(nums):
    for n in nums:
        yield n**2

print(sum(square(fibonacci_numbers(10))))