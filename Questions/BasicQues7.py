#Wite a program using conditional statement to check if a traffic light is red, yellow or green and print appropriate message.
light_color = input("Enter the Traffic light color (red, yellow, green): ").lower()
if light_color == "red":
    print("Stop! the light is red.")
elif light_color == "yellow":
    print("Slow down! the light is yellow.")
elif light_color == "green":
    print("Go! the light is green.")
else:
    print("Invalid traffic light color entered.")