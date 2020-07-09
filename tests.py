import calc
import data 

data.total_budget = input("What is your budget? ")
data.duration = input("How many days are you staying? ")

# set_travel tests
# no housing preference
'''
print(calc.set_travel()) # print our input
print(calc.travel_expenses) # print 2x the price of our input
'''

# set_housing tests
# no travel preference
'''
print(calc.set_housing()) # print our input
'''
# with travel preference
calc.travel_choice = input("What is your travel preference? (If none, press ENTER.) ")
print(calc.set_housing())