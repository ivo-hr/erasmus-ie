from math import inf
def calculate(input_string):
    try:
        splitInput = input_string.split(',')
        numbers = [None] * (len(splitInput) - 1)
        operation = ''
        for i in range(len(splitInput)):
            if splitInput[i].strip() in ['+', '-', '*', '/']:
                # Code to handle when it's an operation
                operation = splitInput[i].strip()
                print("Input", i, "is an operation.\n Value:", operation)
            else:
                try:
                    # Code to handle when it's a number
                    numbers[i] = float(splitInput[i].strip())
                    print("Input", i, "is a digit.\n Value:", numbers[i])

                except ValueError:
                    print("Input", i, "is not a digit or operation, ignoring.\n Value:", splitInput[i])
        
        #Clean up the numbers list
        numbers = [x for x in numbers if x is not None]
        
        if len(numbers) < 2:
            raise ValueError("Too few numbers to perform operation. Please enter at least 2 numbers.")
        elif len(numbers) > 4:
            numbers = numbers[:4]
            print("Too many numbers. Only the first 4 will be used.")
            
        if operation == '+':
            result = sum(numbers)
        elif operation == '-':
            result = float(numbers[0]) - float(numbers[1])
        elif operation == '*':
            result = 1
            for num in numbers:
                result *= float(num)
        elif operation == '/':
            if float(numbers[1]) == 0 and float(numbers[0]) >= 0:
                result = inf
            elif float(numbers[1]) == 0 and float(numbers[0]) < 0:
                result = -inf
            else: 
                result = float(numbers[0]) / float(numbers[1])
        else:
            result = eval(input_string)
        return result
    except Exception as e:
        return f"Error: {str(e)}"


#Run the calculator
#print(calculate(input("Enter the numbers and operation separated by a comma: ")))