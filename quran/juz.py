import random
import math

def select_and_input():
    # Define the list of options
    options = [5, 10, 15, 20, 25, 30]

    # Display the options to the user
    print("Select a number from the following options:")
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")

    # Prompt the user to choose an option
    choice = input("Enter the number corresponding to your choice: ")

    # Check if the choice is a valid integer
    if choice.isdigit():
        choice = int(choice)

        # Check if the choice is within the valid range
        if 1 <= choice <= len(options):
            selected_value = options[choice - 1]
            user_input_set = set()  # Create an empty set to store user inputs

            # If the selected value is 30, fill the set with numbers from 1 to 30
            if selected_value == 30:
                user_input_set.update(range(1, 31))
            else:
                # Prompt the user to enter unique numbers within the specified range
                while len(user_input_set) < selected_value:
                    user_input = input(f"Enter a unique number between 1 and 30 ({len(user_input_set) + 1}/{selected_value}): ")

                    # Check if the input is a valid integer within the range
                    if user_input.isdigit():
                        user_input = int(user_input)

                        if 1 <= user_input <= 30 and user_input not in user_input_set:
                            user_input_set.add(user_input)
                        else:
                            print("Invalid input. Please enter a unique number within the specified range.")
                    else:
                        print("Invalid input. Please enter a valid number.")

            # Print the set of user inputs
            print("User inputs:", user_input_set)

            # Determine the number of random numbers to select based on the set length divided by 2
            num_random_numbers = math.ceil(len(user_input_set) / 2)

            # Select the specified number of random numbers from the user input set
            selected_random_numbers = random.sample(user_input_set, num_random_numbers)

            # Print the selected random numbers
            print(f"If the set length is {len(user_input_set)}, select {num_random_numbers} numbers from it randomly:")
            for num in selected_random_numbers:
                print(num)
        else:
            print("Invalid choice. Please select a number from the provided options.")
    else:
        print("Invalid input. Please enter a valid number.")

# Call the function to run it
select_and_input()
