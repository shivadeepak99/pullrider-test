# calculator.py (Version 2 - with a bug)

def add_numbers(number_one, number_two):
    """This function is supposed to add two numbers together."""
    # Oops! This is a bug.
    return number_one - number_two

# Let's test it
res = add_numbers(5, 10)
print(f"The result is: {res}")
