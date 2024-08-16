from art import logo

print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def the_calculation(operation_tp, num_1, num_2):
    calculation_function = operations[operation_tp]
    return calculation_function(num_1, num_2)

def calculator():
    number_1 = float(input("What's the first number? "))
    for keys in operations:
        print(keys)
    operation_type = input("Which of these operations you want to do? ").strip()
    number_2 = float(input("What's the second number? "))

    first_answer = the_calculation(operation_type, number_1, number_2)
    print(f"{number_1} {operation_type} {number_2} = {first_answer}")

    continue_calculation = input(f"Type 'y' to continue calculating with {first_answer}, or type 'n' to exit: ") == 'y'

    while continue_calculation:
        operation_type = input("Pick another operation: ").strip()
        number_3 = float(input("Choose another number: "))

        second_answer = the_calculation(operation_type, first_answer, number_3)

        print(f"{first_answer} {operation_type} {number_3} = {second_answer}")

        continue_calculation = input(f"Type 'y' to continue calculating with {second_answer}, or type 'n' to exit: ") == 'y'
        if continue_calculation:
            first_answer = second_answer
        else:
            calculator()

calculator()