def get_student_score():
    """
    Function to prompt the user for their score and ensure it's a valid numeric value.
    Returns:
        float: The valid score entered by the user.
    """
    score = input("Enter your score: ")
    
    try:
        # Convert the input to a float
        score = float(score)
        return score
    except ValueError:
        # If the input is not a valid number, print an error message and ask again
        print("Invalid input. Please enter a valid numeric score.")
        return get_student_score()  # Recursive call to prompt again

def calculate_grade(score):
    """
    Function to calculate the grade based on the score.
    Args:
        score (float): The student's score.
    Returns:
        str: The letter grade corresponding to the score.
    """
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def main():
    """
    Main function to get the score, calculate the grade, and display the result.
    """
    # Step 1: Get the score from the user
    score = get_student_score()
    
    # Step 2: Calculate the grade
    grade = calculate_grade(score)
    
    # Step 3: Display the grade
    print(f"Your Grade is: {grade}")

if __name__ == "__main__":
    
