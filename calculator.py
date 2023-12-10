def calculator(operation, num1, num2):
    if operation == 'add' :
        result = num1 + num2
    elif operation == 'subtract' :
        result = num1 - num2
    elif operation == 'multiply' :
        result = num1 * num2
    elif operation == 'divide' :
        if num2 != 0:
            result = num1 / num2
        else: result = "Error! division by zero"
    elif operation == 'power' :
        result = num1 ** num2
    else: result = "Invalid operation"
    return result

print(calculator('divide', 5, 3))