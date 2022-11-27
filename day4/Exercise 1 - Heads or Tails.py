#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
	 
#Write the rest of your code below this line 👇
import random

randomFloat = random.random()
randomInteger = round(randomFloat)


if randomInteger == 1:
    print("Heads")
else:
    print("Tails")    
