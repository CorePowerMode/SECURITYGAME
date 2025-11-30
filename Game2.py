# Start of everything
player_score = 0
wining_score = 100
total_scenarios = 0
scenarios_passed = 0
scenarios_list = []


def show_instructions():
    print("Instructions")

def askPlayer():
    userInput = input("Are you ready to play? (Y/N) ")
    if userInput.upper == "Y":
        print("Great, lets play!")
    else:
        exit()



# Loading Files
with open("scenarios.txt", "r") as scenarioFile:
    for line in scenarioFile:
        scenarios_list.append(line)


permissionFile = open("scenarios.txt", "r")
permission_guide = permissionFile.read()
permissionFile.close()




# Permission Guide and Scenarios
def display_permissions_guide():
    print(permission_guide)

scenario_index = 0

def present_scenario():
   line = scenarios_list[scenario_index]
   scenarioLine = line.split(",")

   scenarioNum = scenarioLine[0]
   role = scenarioLine[1]
   description = scenarioLine[2]

   print(f"Scenario: {scenarioNum}")
   print(f"Role: {role}")
   print(f"Description: {description}")




def get_player_permission_choice():
    print("1 - Read, 2 - Write, 3 - Execute, 4 - Admin, 5 - No Acess")

    # CODE TO FILL



# Evaluation, Statistics, and Update
def evaluate_permissions(selected_permissions, correct_permissions):
    global scenarios_passed
    points_earned = 0

    if selected_permissions == correct_permissions:
        print("+20 points!")
        points_earned += 20
        scenarios_passed = scenarios_passed + 1

    elif len(selected_permissions) > len(correct_permissions):
        print("Too many permissions")
        points_earned -= 10

    elif len(selected_permissions) < len(correct_permissions):
        print("Feedback")
        points_earned -= 5

    print(f"Correct permissions for this is {correct_permissions}")

    return points_earned



def display_statistics():
    accuracy = float(scenarios_passed / total_scenarios * 100)
    print(f"Your total scenario completed is {total_scenarios}")
    print(f"Your accuracy percentage is {accuracy}")
    print("Education Tip...")



def update_score(points_earned):
    global player_score
    global total_scenarios

    player_score = player_score + points_earned
    
    total_scenarios = total_scenarios + 1

    print(player_score)





# Main Game Loop

def main():
    '''
    CODE TO FILL


    '''
    






    









