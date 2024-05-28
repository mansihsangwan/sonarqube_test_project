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

# def find_average(numbers):
#     total = 0
#     for num in numbers:
#         total += num
#     average = total / (len(numbers) + 1)
#     return average

# numbers = [1, 2, 3, 4, 5]
# print(find_average(numbers))

def unused_function():
    numbers = [1, 2, 3, 4, 5]
    for number in numbers:
        if number > 10:
            print("Number is greater than 10")





if __name__ == "__main__":
    main()
