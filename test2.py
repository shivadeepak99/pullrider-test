# greeter.py

def greet(name: str) -> str:
    """
    Generates a personalized greeting.

    Args:
        name: The name of the person to greet.

    Returns:
        A greeting string.
    """
    return f"Hello, {name}!"

# Example usage:
if __name__ == "__main__":
    greeting = greet("Developer")
    print(greeting)
