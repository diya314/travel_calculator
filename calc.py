import data

# input variables 
total_budget = 0
duration = 0
def set_inputs():
    global total_budget, duration 
    total_budget = int(input("What is your budget? "))
    duration = int(input("How many days are you staying? "))

# function-set variables
total_expenses = 0
travel_expenses = 0
travel_choice = ""
housing_choice = ""

def set_travel():
    global travel_choice, housing_choice

    # no housing preference
    if len(housing_choice) == 0: 
        travel_choice = input("What is your preferred mode of transport? ")
        set_travel_expenses()
    
    return travel_choice


def set_travel_expenses():
    global travel_expenses, travel_choice
    travel_expenses = data.travel[travel_choice] * 2
    return travel_expenses


def set_housing():
    global travel_choice, housing_choice, travel_expenses, total_budget
    # no travel preference
    if len(travel_choice) == 0: 
        housing_choice = input("What is your preferred type of housing? ")
        return housing_choice
    
    # with travel preference 
    h_budget = total_budget - set_travel_expenses()
    print("total budget: " + str(total_budget))
    print("housing budget: " + str(h_budget))
    if duration * data.housing["expensive"] <= h_budget: # if can afford expensive housing
        housing_choice = "expensive"
    elif duration * data.housing["cheap"] <= h_budget: # if can afford cheap housing
        housing_choice = "cheap"
    else:
        return "You can't afford housing! :(( "
    return housing_choice
    