from calculator import Calculator

def main():
    calc = Calculator()
    
    print("Simple Calculator")
    print("Available operations: +, -, *, /")
    print("Type 'quit' to exit")
    
    while True:
        try:
            # Get user input
            expression = input("\nEnter calculation (e.g., 5 + 3): ")
            
            # Check for quit command
            if expression.lower() == 'quit':
                print("Goodbye!")
                break
            
            # Parse the input
            num1, operator, num2 = expression.split()
            num1 = float(num1)
            num2 = float(num2)
            
            # Perform calculation
            if operator == '+':
                result = calc.add(num1, num2)
            elif operator == '-':
                result = calc.subtract(num1, num2)
            elif operator == '*':
                result = calc.multiply(num1, num2)
            elif operator == '/':
                result = calc.divide(num1, num2)
            else:
                print("Invalid operator! Use +, -, *, or /")
                continue
                
            print(f"Result: {result}")
            
        except ValueError as e:
            if str(e) == "Cannot divide by zero":
                print("Error: Cannot divide by zero!")
            else:
                print("Error: Please enter valid numbers and operator separated by spaces")
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
