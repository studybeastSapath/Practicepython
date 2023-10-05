#Ask user their name
name= input("What's the name of the user ? ")

#Remove all whitespaces and capitalise the first letter of the name and title of the user input
name= name.strip().title()

#Greet the user
print(f"Hello, {name}")
