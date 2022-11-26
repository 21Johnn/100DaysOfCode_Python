# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

letter_countT = ((name1 + name2).lower()).count("t")
letter_countR = ((name1 + name2).lower()).count("r")
letter_countU = ((name1 + name2).lower()).count("u")
letter_countE = ((name1 + name2).lower()).count("e")
total1 = letter_countT + letter_countR + letter_countU + letter_countE

letter_countL = ((name1 + name2).lower()).count("l")
letter_countO = ((name1 + name2).lower()).count("o")
letter_countV = ((name1 + name2).lower()).count("v")
letter_countE = ((name1 + name2).lower()).count("e")
total2 = letter_countL + letter_countO + letter_countV + letter_countE
score = int (str(total1) + str(total2))

if score <10 or score>90:
    print (f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score<=50:
    print (f"Your score is {score}, you are alright together.")
else:
    print (f"Your score is {score}.")