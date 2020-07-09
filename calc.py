import data

total_budget = input("What is your budget? ")
duration = input("How many days are you staying? ")
total_expenses = 0
travel_expenses = 0

travel_choice = ""
housing_choice = ""

def set_travel():
    global travel_choice, housing_choice
    if len(housing_choice) == 0: # no preference
        travel_choice = input("What is your preferred mode of transport? ")
        set_travel_expenses()
        return travel_choice
    

def set_travel_expenses():
    global travel_expenses
    travel_expenses = data.travel[travel_choice] * 2

def calc_housing():
    global travel_choice, housing_choice, travel_expenses
    if len(travel_choice) == 0: # no preference
        housing_choice = input("What is your preferred type of housing? ")
    h_budget = total_budget - travel_expenses