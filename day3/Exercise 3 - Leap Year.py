# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

year_by_4 = year % 4 
year_by_100 = year % 100
year_by_400 = year % 400

#Write your code below this line 👇
if year % 4 == 0 and year_by_100 != 0 or year_by_100 == 0 and year_by_400 == 0:
    print("Leap year.")
else:
    print("Not leap year.")    
    

