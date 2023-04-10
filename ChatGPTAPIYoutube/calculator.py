def calculator():
    # Get user input for the first number
    num1 = float(input("Enter the first number: "))
    
    # Get user input for the operation
    operation = input("Enter the operation (+, -, *, /): ")
    
    # Get user input for the second number
    num2 = float(input("Enter the second number: "))
    
    # Perform the operation based on user input
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    else:
        print("Invalid operation, please try again.")
        return

    # Print the result
    print("Result:", result)

# Call the calculator function
calculator()
