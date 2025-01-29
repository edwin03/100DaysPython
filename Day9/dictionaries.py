programming_dictionary = {
"Bug": "An error in a program that prevents the program from running as expected.", 
"Function": "A piece of code that you can easily call over and over again.",
}

# Retrive by using the key
print(programming_dictionary["Bug"])

# adding to a dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."

# Creating an empty/wiping dictionary
empty_dictionary = []

# editing an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"

# Looping in a dictionary, this prints the keys
for thing in programming_dictionary:
	# This makes it to print the values
	print(programming_dictionary[thing])

print(programming_dictionary)# editing an item in a dictionary
programming_dictionary["Bug"] = "Assigining something else."