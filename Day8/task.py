def greet():
	print("Hello!")
	print("World")
	print("Hi Edwin")

greet()

# Function that allows for inputs
def greet_with_name(name):
	print(f"Hello {name}")

greet_with_name("Edwin")

#Function with multiple inputs
def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}?")

# This is pos  
greet_with("Edwin", "Houston")