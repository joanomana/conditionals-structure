def calculate_bmi(weight, height):
    return weight / (height ** 2)

def determine_risk(age, bmi):
    if age < 45:
        if bmi < 22.0:
            return "low"
        else:
            return "medium"
    else:
        if bmi < 22.0:
            return "medium"
        else:
            return "high"

def main():
    height = float(input("Enter height in meters: "))
    weight = float(input("Enter weight in kilograms: "))
    age = int(input("Enter age in years: "))

    bmi = calculate_bmi(weight, height)
    risk = determine_risk(age, bmi)

    print(f"Your coronary disease risk is: {risk}")

if __name__ == "__main__":
    main()