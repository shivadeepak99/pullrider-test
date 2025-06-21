def get_even_numbers(max_number):
    """Returns a list of even numbers up to max_number."""
    even_numbers = []
    for i in range(max_number + 1):
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers
#
