def main():
    print("Starting the application...")

    # Importing here to create a cyclic import issue
    from app import calculator

    result = calculator.add(5, 3)
    print(f"Result of addition: {result}")

    # Unreachable code
    return

    result = calculator.divide(5, 0)  # This will cause a division by zero error
    print(f"Result of division: {result}")

if __name__ == "__main__":
    main()
