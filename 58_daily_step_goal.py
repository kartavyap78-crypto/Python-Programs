# 5. Daily Steps Goal

# Ask the user to enter daily steps goal and steps walked.

# Display whether the goal is achieved or not.

step_goal = int(input("enter a goal = "))
step_walked = int(input("enter step walked = "))

if step_goal == step_walked:
    print("goal is achieved")
else:
    print("goal is not achieved")