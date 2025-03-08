def get_student_score() -> float:
    """
    Asks the user to input a score between 0 and 100.
    
    If the input is invalid (not a number or out of range), it will ask again until 
    a valid score is provided.
    
    Returns:
        float: The valid score entered by the user.
    """
    while True:
        try:
            score = float(input("Enter your score: "))
            if 0 <= score <= 100:
                return score
            print("Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculate_grade(score: float) -> str:
    """
    Returns the letter grade based on the score.
    
    A: 90+, B: 80-89, C: 70-79, D: 60-69, F: below 60.
    
    Args:
        score (float): The score to calculate the grade for.
    
    Returns:
        str: The letter grade.
    """
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"

def main():
    """
    Gets the student's score and shows their grade.
    """
    student_score = get_student_score()  # Get the score
    grade = calculate_grade(student_score)  # Get the grade
    print(f"Your Grade is: {grade}")  # Output the grade

if __name__ == "__main__":
    main()
