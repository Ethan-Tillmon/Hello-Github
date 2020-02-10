# three daata types at input

# string
phrase = input("Enter aa string: ")
print("You said " + phrase)
print(f"You said {phrase}")

# float
someFloat = float(input("Enter a float: "))
print("You entered float: " + str(someFloat))
print(f"You entered float: {someFloat}")

# int
someInt = float(input("Enter an int: "))
print("You entered int: " + str(someInt))
print(f"You entered int: {someInt}")

# string interpolation is sweet
print(f"Do Python inline, like this {someFloat} * {someInt} = {someFloat * someInt}")