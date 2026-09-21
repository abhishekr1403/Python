# Using following list of cities per country,
# india = ["mumbai", "banglore", "chennai", "delhi"]
# pakistan = ["lahore","karachi","islamabad"]
# bangladesh = ["dhaka", "khulna", "rangpur"]
# Write a program that asks user to enter a city name and it should tell which country the city belongs to
# Write a program that asks user to enter two cities and it tells you if they both are in same country or not. For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print "They don't belong to same country"


india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

# city = input('Enter a city: ')
# if city in india:
#     print(f'{city} belongs to the country india')
# elif city in pakistan:
#     print(f'{city} belongs to the country pakistan')
# elif city in bangladesh:
#     print(f'{city} belongs to the country bangladesh')
# else:
#     print(f"Sorry, i don't know which country, {city} belongs to. ")

# city1 = input("Enter city 1 : ")
# city2 = input("Enter city 2 : ")
#
# if city1 in india and city2 in india:
#     print(f"{city1} and {city2} are both in India")
# elif city1 in pakistan and city2 in pakistan:
#     print(f"{city1} and {city2} are both in Pakistan")
# elif city1 in bangladesh and city2 in bangladesh:
#     print(f"{city1} and {city2} are both in Bangladesh")
# else:
#     print("They don't belong to same country")


## Exercise: Python If Condition
# 2. Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
#     1. Ask user to enter his fasting sugar level
#     2. If it is below 80 to 100 range then print that sugar is low
#     3. If it is above 100 then print that it is high otherwise print that it is normal

sugar_level = float(input("Enter your fasting sugar level: "))
if sugar_level < 80:
    print('Your sugar level is low!')
elif sugar_level > 100:
    print('Your sugar level is high!')
else:
    print('Your sugar level is normal!')