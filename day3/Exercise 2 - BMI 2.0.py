# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = float(weight / (height * height))
bmi_round = round(bmi)
bmi_round_str = str(bmi_round)

if bmi_round <= 18.5:
    print(f"Your BMI is {bmi_round_str}, you are underweight.")
elif bmi_round > 18.5 and bmi_round < 25:
    print(f"Your BMI is {bmi_round_str}, you have a normal weight.")
elif bmi_round > 25 and bmi_round < 30: 
    print(f"Your BMI is {bmi_round_str}, you are slightly overweight.")
elif bmi_round > 30 and bmi_round < 35:     
    print(f"Your BMI is {bmi_round_str}, you are obese.")
else:
    print(f"Your BMI is {bmi_round_str}, you are clinically obese.")
