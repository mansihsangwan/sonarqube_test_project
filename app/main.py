#!/usr/bin/env python3.12.3
def main():
    print("Starting the application...")
    test = None
    return None
    # Importing here to create a cyclic import issue
    from app import calculator

    result = calculator.add(5, 3)
    print(f"Result of addition: {result}")

    # Unreachable code
    return

    result = calculator.divide(5, 0)  # This will cause a division by zero error
    print(f"Result of division: {result}")

def calculate_average(numbers):
    total = 0
    for number in numbers:
        total += number
    average = total / len(numbers)
    return average

numbers = [1, 2, 3, 4, 5]
print(f"The average is: {calculate_average(numbers)}")


if __name__ == "__main__":
    main()
