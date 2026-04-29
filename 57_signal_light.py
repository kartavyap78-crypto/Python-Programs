# 32. Write a Python program that will check for the following conditions:
# •	If the light is green: Car is allowed to go.
# •	If the light is yellow: Car has to wait.
# •	If the light is red: Car has to stop.
# •	Other signal: Unrecognized signal (e.g., black, blue, etc.)

light = input("enter a light colour = ")

if light == 'Green':
    print("Car is allowed to go")
elif light == 'Yellow':
    print("car has to wait")
elif light == 'Red':
    print("car has to stop")
else:
    print("Unrecognized signal")