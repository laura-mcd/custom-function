# Define the function
def add_nums(a, b):
    """
    Calculate the sum of two numbers.
    
    Parameters:
    number (int): Numbers to be added must be integers.
    
    Returns:
    int: Sum of the two numbers.
    """
    # Function logic to add two numbers
    result = a + b  
    return result

# Ask the user to input numbers for a and b
a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))

# Call the addition function with a=7 and b=3
result = add_nums(a, b)
# Print with format "result: sum"
print(f"Result: {result}")
