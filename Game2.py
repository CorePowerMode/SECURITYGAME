player_score = 0
winning_score = 100
total_scenarios = 0
scenarios_passed = 0
scenarios_list = []
scenario_index = 0



def show_instructions():
    print("""Instructions
          1.....
          2.....
          3.....
          4.....
          5.....
          6.....
          7.....
          """)
    


def scenarios_File():
    with open("scenarios.txt", "r") as scenarioFile:
        for line in scenarioFile:
            line = line.strip()
            if line:
                scenarios_list.append(line)


def permissionGuide():
    permissionFile = open("permission_guide.txt", "r")
    permissionText = permissionFile.read()
    permissionFile.close()
    return permissionText


def display_permissions_guide(permissionGuide):
    print(permissionGuide)
    

def present_scenario():
   global scenario_index
   global player_score
   line = scenarios_list[scenario_index]
   scenarioLine = line.split("|")
   
   

   scenarioNum = scenarioLine[0].strip()
   role = scenarioLine[1].strip()
   description = scenarioLine[2].strip()

   print(f"Scenario: {scenarioNum}")
   print(f"Role: {role}")
   print(f"Description: {description}")
   print(f"Current Score: {player_score}/100")



def get_player_permission_choice():
    print("1 - Read, 2 - Write, 3 - Execute, 4 - Admin, 5 - No Acess")
    choices = ["1", "2", "3", "4", "5"]
    

    while True:
        permissionInput = input("Please enter a number and space them out: ")
        listPermissionInput = permissionInput.split()

        correct = True

        for numbers in range(len(listPermissionInput)):
            num = listPermissionInput[numbers]

            if num not in choices:
                print("Invalid, pelase enter number between 1 and 5")
                correct = False
                break
            
            for duplicates in range(numbers + 1, len(listPermissionInput)):
                if num == listPermissionInput[duplicates]:
                    print("No duplicate numbers allowed, one permission each.")
                    correct = False
                    break

            if not correct:
                break

        if correct:
            break
        else:
            ("Try again")

    return listPermissionInput

    
def evaluate_permissions(selected_permissions, correct_permissions):
    global scenarios_passed
    points_earned = 0

    if selected_permissions == correct_permissions:
        print("+20 points!")
        points_earned += 20
        scenarios_passed += 1

    elif len(selected_permissions) > len(correct_permissions):
        print("Too many permissions")
        points_earned -= 10

    elif len(selected_permissions) < len(correct_permissions):
        points_earned -= 5

    print(f"Correct permissions for this is {correct_permissions}")

    return points_earned


def update_score(points_earned):
    global player_score
    global total_scenarios

    player_score = player_score + points_earned
    
    total_scenarios = total_scenarios + 1

    print(player_score)


def display_statistics():
    accuracy = float(scenarios_passed / total_scenarios * 100)
    print(f"Your total scenario completed is {total_scenarios}")
    print(f"Your accuracy percentage is {accuracy}")
    print("Education Tip...")


# Main Game Loop

def main():
    global scenario_index
    global player_score
    global total_scenarios
    global scenarios_passed
    scenario_index = 0
    scenarios_passed = 0
    total_scenarios = 0
    player_score = 0

    show_instructions()

    input("Press enter to continue")

    askReady = input("Type (y) to start or type (x) to exit: ")
    if askReady.upper() == "y":
        print("Continuing...")
    elif askReady.upper() == "x":
        print("Exiting...")
        exit()

    scenarios_File()


    guide = permissionGuide()
    display_permissions_guide(guide)

    input("Press enter to continue")

    while scenario_index < len(scenarios_list):
        if player_score >= winning_score:
            print("You reached 100 points! You Win!")
            break
        if player_score < 0:
            print("Your score dropped below 0. Game Over.")
            break

        present_scenario()

    

        correct_permissions = scenarios_list[scenario_index].split("|")[-1].split()

        selected = get_player_permission_choice()
        earned = evaluate_permissions(selected, correct_permissions)
        update_score(earned)

        scenario_index += 1

        display_statistics()


    play_again = str(input("Do you want to play again? [Y/N]:  "))
    if play_again.upper() == "Y":
        print("Play again...")
        main()
    elif play_again.upper() == "N":
        print("Exiting game...")
        exit()

main()
