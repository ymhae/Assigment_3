def get_input():
    """
    Function to safely input two integers from the user.
    """
    while True:
        try:
            a = int(input("Enter the first positive integer: "))
            b = int(input("Enter the second positive integer: "))
            if a > 0 and b > 0:
                return a, b
            else:
                print("Both numbers must be positive integers. Please try again.")
        except ValueError:
            print("Invalid input; please enter valid integers.")

def main():
    a, b = get_input()
    print(f"The GCD of {a} and {b} is {euclidean_algorithm(a, b)}.")

if __name__ == "__main__":
    main()
