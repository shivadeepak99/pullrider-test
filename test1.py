# Get all even numbers from a list
def get_evens(numbers):
    evens = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    return evens
def calculate_sum(a, b):
    # This function has no docstring and uses print
    total = a + b
    print(f"The total is: {total}")
    return total
