def calculate_bmi(weight, height):
    """Calculate the BMI given weight (kg) and height (m)."""
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    """Classify the BMI value into categories."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obesity"

def main():
    print("Welcome to the BMI Calculator!")
    
    try:
        weight = float(input("Please enter your weight in kilograms: "))
        height = float(input("Please enter your height in meters: "))
        
        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)
        
        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"This means you are classified as: {category}")
    except ValueError:
        print("Invalid input. Please make sure to enter numeric values for weight and height.")

if __name__ == "__main__":
    main()
