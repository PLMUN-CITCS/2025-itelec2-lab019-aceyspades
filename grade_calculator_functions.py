def get_student_score() -> float:
    while True:
        try:
            score = float(input("Enter your score: "))
            return score
        except ValueError:
            print("Invalid input. Please enter a valid numerical score.")

def calculate_grade(score: float) -> str:
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
    score = get_student_score()
    grade = calculate_grade(score)
    print(f"Your Grade is: {grade}")

if __name__ == "__main__":
    main()

