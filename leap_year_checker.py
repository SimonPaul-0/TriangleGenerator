def main():
    n = int(input("Enter the size of the diamond (odd number): "))

    if n % 2 == 0:
        print("Invalid input. Please enter an odd number for symmetry.")
        return  # Exit with an error code

    # Print the upper part of the diamond
    for i in range(1, n + 1, 2):
        spaces = (n - i) // 2

        # Print leading spaces
        print(" " * spaces, end="")

        # Print asterisks
        print("*" * i)

    # Print the lower part of the diamond
    for i in range(n - 2, 0, -2):
        spaces = (n - i) // 2

        # Print leading spaces
        print(" " * spaces, end="")

        # Print asterisks
        print("*" * i)

if __name__ == "__main__":
    main()
