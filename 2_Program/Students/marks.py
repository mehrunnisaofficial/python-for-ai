
def total_subjects():
    """
    Ask the user for the number of subjects.
    """

    while True:
        try:
            # Get the number of subjects from the user
            count = int(
                input("Enter how many subjects you wanna add: ")
            )

            # Check whether the number is positive
            if count <= 0:
                print("Please enter a positive number.")
                continue

            # Return the valid subject count
            return count

        except ValueError:
            # Handle non-numeric input
            print("Invalid Entry. Please enter a number.")


def get_subjects(total):
    """
    Collect subject names and marks.

    Returns:
        dict: Subject names and their gained marks.
    """

    subjects = {}

    # Loop through each subject
    for i in range(1, total + 1):

        # Get the subject name
        while True:
            subject = input(
                f"Enter Subject {i} name: "
            ).strip().capitalize()

            # Check whether the name is empty
            if not subject:
                print("Subject name cannot be empty.")
                continue

            # Prevent duplicate subject names
            if subject in subjects:
                print("Subject already exists. Please enter another.")
                continue

            if not subject.isalpha():
                print("please enter correct name")
                continue

            break

        # Get marks for the subject
        while True:
            try:
                marks = int(
                    input(f"Enter marks of {subject}: ")
                )

                # Marks must be between 0 and 100
                if marks < 0 or marks > 100:
                    print("Please enter marks between 0 and 100.")
                    continue

                # Exit the marks validation loop
                break

            except ValueError:
                # Handle non-numeric input
                print("Invalid Entry. Please enter a number.")

        # Store subject and marks in the dictionary
        subjects[subject] = marks

    # Return the complete dictionary
    return subjects


def mark_calc(marks):
    """
    Calculate total, average, and percentage.

    Args:
        marks: An iterable containing marks.

    Returns:
        tuple: Total marks, average, and percentage.
    """

    # Convert marks into a list
    marks = list(marks)

    # Calculate the total gained marks
    total = sum(marks)

    # Calculate the average marks
    average = total / len(marks)

    # Calculate the total maximum marks
    total_actual = len(marks) * 100

    # Calculate the percentage
    percentage = (total / total_actual) * 100

    # Return all three calculated values
    return total, average, percentage


def show(name):
    """
    Collect student marks and display a formatted table.
    """

    # Get the number of subjects
    total_count = total_subjects()

    # Collect subject names and marks
    subjects = get_subjects(total_count)

    # Calculate total, average, and percentage
    total, average, percent = mark_calc(
        subjects.values()
    )

    # Display the table header
    print(f"{name.upper():^15}")
    print()
    print(
        f"{'Subject':<15}"
        f"{'Actual Marks':<15}"
        f"{'Gained Marks':<15}"
    )

    # Print a separator line
    print("-" * 45)

    # Display each subject and its marks
    for subject, marks in subjects.items():
        print(
            f"{subject:<15}"
            f"{100:<15}"
            f"{marks:<15}"
        )

    # Calculate total actual marks
    total_actual = len(subjects) * 100

    # Print a separator before the total
    print("-" * 45)

    # Display total actual and gained marks
    print(
        f"{'Total':<15}"
        f"{total_actual:<15}"
        f"{total:<15}"
    )

    # Display average and percentage
    print()
    print(f"Average: {average:.2f}")
    print(f"Percentage: {percent:.2f}%")


# Run the program when this file is executed directly
if __name__ == "__main__":
    show()


# i am not getting it