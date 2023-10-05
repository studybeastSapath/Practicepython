#Convert the first letters of the user's name and title to capital letters

#Ask the user for their name
name = input("What's your name?")

#Remove whitespace from the user's input
name= name.strip()

#Capitalise the user's input
name=name.capitalize()

#Greet the user
print(f"Hello ,{name}")
