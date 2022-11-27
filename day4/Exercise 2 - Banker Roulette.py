# Import the random module here

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random


len_names = int(len(names) - 1)
random_index = random.randint(0 , len_names)
random_name = names[random_index]

print(f"{random_name} is going to buy the meal today!")






