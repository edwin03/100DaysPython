# import turtle, prettytable
# from turtle import Turtle, Screen

# timmy = turtle.Turtle()
# print(timmy)
# timmy.shape('turtle')
# timmy.color("DarkGreen")
# timmy.forward(100)

# my_screen = turtle.Screen()

# # accessing the attributes, by entering the name of th object then the attribute name.
# print(my_screen.canvheight)

# # accessing object methods, by enerting the name of the object then then the method.
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokeon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)