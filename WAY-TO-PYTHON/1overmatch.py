# Importing random library as r
import random as r

# Taking the required inputs
T1 = input("Enter the name of team 1: ") 
T2 = input("Enter the name of team 2: ")
P = int(input("Enter the number of players per team: "))
Wickets = P - 1  # Total wickets a team can lose

print("\nThe name of team 1 is:", T1)
print("The name of team 2 is:", T2)
print("The number of players from each team are:", P)

# List for the toss
Teams = [T1, T2]

# Toss logic
TossQ = input("Are you ready for the toss? (Y/N): ").upper()

while TossQ != "Y":
    TossQ = input("Please enter 'Y' to proceed with the toss: ").upper()

# Toss winner and their decision
TossWinner = r.choice(Teams)
print("The toss winner is Team:", TossWinner)

# Get the toss loser by removing the winner from the list
TossLoser = [team for team in Teams if team != TossWinner][0]
print("The toss loser is Team:", TossLoser)

BatOrBowl = ["Bat", "Ball"]
bobresult = r.choice(BatOrBowl)
print(TossWinner, "decided to", bobresult.lower())

# Assign who bats first and who bowls first
if bobresult == "Bat":
    first_batting_team = TossWinner
    second_batting_team = TossLoser
else:
    first_batting_team = TossLoser
    second_batting_team = TossWinner

print(f"Now {first_batting_team} will bat first and {second_batting_team} will bat second.")

# Function to simulate one over for a team
def play_one_over(team_name):
    cur_wicket = 0
    cur_runs = 0
    cur_balls = 0

    Ball_outcomes = ["wicket", "wide", "no-ball", 0, 1, 2, 3, 4, 6]

    print(f"\n{team_name} is now batting:")

    while cur_balls < 6 and cur_wicket < Wickets:
        ball = r.choice(Ball_outcomes)
        
        # Display ball number and outcome
        print(f"Ball {cur_balls + 1}: {ball}")
        
        if ball == "wicket":
            cur_wicket += 1
            print(f"Wicket down! Current wickets: {cur_wicket}")
        elif ball == "wide" or ball == "no-ball":
            cur_runs += 1
            print(f"Extra run! Current runs: {cur_runs}")
            print(f"Extra ball due to {ball}")
        else:
            cur_runs += ball
            print(f"Runs scored: {ball}. Current runs: {cur_runs}")
            cur_balls += 1  # Valid ball

    # Return the team's score and wickets after the over
    print(f"\n{team_name} finished with {cur_runs} runs and {cur_wicket} wickets lost.")
    return cur_runs, cur_wicket

# Play one over for the first batting team
first_team_runs, first_team_wickets = play_one_over(first_batting_team)

# Play one over for the second batting team
second_team_runs, second_team_wickets = play_one_over(second_batting_team)

# Declare the winner based on the scores
print("\nMatch Summary:")
print(f"{first_batting_team}: {first_team_runs} runs, {first_team_wickets} wickets")
print(f"{second_batting_team}: {second_team_runs} runs, {second_team_wickets} wickets")

if first_team_runs > second_team_runs:
    print(f"\n{first_batting_team} wins by {first_team_runs - second_team_runs} runs!")
elif second_team_runs > first_team_runs:
    print(f"\n{second_batting_team} wins by {P - 1 - second_team_wickets} wickets!")
else:
    print("\nIt's a tie!")

