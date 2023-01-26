from colorama import init, Fore
init()

print("BMI Calculator")

weight = float(input("Enter your body weight (kg): "))
height = float(input("Enter your height (m): "))
print("\n")

bmi = round(weight / height**2, 1)

if bmi < 18.5:
    print(Fore.RED + f"BMI => {bmi}, Status => Underweight")
elif bmi >= 18.5 and bmi < 25:
    print(Fore.GREEN + f"BMI => {bmi}, Status => Normal")
elif bmi >= 25 and bmi < 30:
    print(Fore.YELLOW + f"BMI => {bmi}, Status => Overweight")
elif bmi >= 30 and bmi < 35:
    print(Fore.RED + f"BMI => {bmi}, Status => Obese")
else:
    print(Fore.RED + f"BMI => {bmi}, Status => Clinically obese")
