def get_student_score():
    """
    Prompts the user to enter the student's score and converts the input to a numeric type.
    Returns:
        float: The student's score as a numeric value.
    """
    score = input("Enter your score: ")
    
    try:
        score = float(score) 
        return score
    except ValueError:
        print("Invalid input. Please enter a valid numeric score.")
        return get_student_score() 

def calculate_grade(score):
    """
    Determines the letter grade based on the given score.
    Args:
        score (float): The score obtained by the student.
    Returns:
        str: The letter grade ('A', 'B', 'C', 'D', or 'F').
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
    Main function that coordinates the process of getting a score, calculating the grade,
    and displaying the result to the user.
    """
    score = get_student_score()
    
    grade = calculate_grade(score)
    
     print(f"Your Grade is: {grade}")

if __name__ == "__main__":
    main()
