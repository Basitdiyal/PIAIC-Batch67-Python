print("Madlibs Python Project")

rabbit_name:str = input("Enter the name of Rabit: ")
turtle_name:str = input("Enter the name of Turtle: ")
adjective1: str = input("Enter the Adjective1: ")
adjective2: str = input ("Enter the Adjective2: ")
race_distance: str= input("Enter the race distance: i.e(Meters) ")
verb: str= input("Enter the Verb: ")
obstacle: str = input("Enter the obstacle: ")
winner:str = input("Enter the Winner Name: ")

madlib = f"""
Once upon a time, there was a {adjective1} rabbit named {rabbit_name} and a {adjective2} turtle named {turtle_name}.
They decided to have a race over a distance of {race_distance}. 

The race began, and {rabbit_name} started {verb} at lightning speed, leaving {turtle_name} far behind. 
But halfway through the race, {rabbit_name} encountered {obstacle} and got distracted. Meanwhile, {turtle_name}, 
steady and determined, kept going without stopping. 

In the end, the winner of the race was... {winner}! Everyone learned that {adjective2} perseverance 
can sometimes outshine {adjective1} speed.
"""

# Print the completed Madlib
print(f"\nHere is your Rabbit and Turtle Race Madlib: {madlib}")
