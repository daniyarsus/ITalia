def add_numbers(x: int, y: int) -> int:
    try:

        """
        This function takes two integers and returns their sum.
        """
        return x + y
    except:
        return Exception

result = add_numbers(5, 3)  # Here, we're providing two integers, and we expect an integer return value.
print(result)  # Output: 8