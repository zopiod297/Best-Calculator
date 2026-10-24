def calculate(first, operator, second):
    if operator == "+":
        return first + second
    if operator == "-":
        return first - second
    if operator == "*":
        return first * second
    if operator == "/":
        if second == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return first / second

    raise ValueError("Unsupported operator. Use +, -, *, or /.")


def main():
    print("Calculator")
    print("Enter q at the operator prompt to quit.")

    while True:
        try:
            first = float(input("First number: "))
            operator = input("Operator (+, -, *, /): ").strip()

            if operator.lower() == "q":
                print("Goodbye!")
                break

            second = float(input("Second number: "))
            print("Result:", calculate(first, operator, second))

        except ValueError as error:
            print("Invalid input:", error)
        except ZeroDivisionError as error:
            print(error)


if __name__ == "__main__":
    main()
