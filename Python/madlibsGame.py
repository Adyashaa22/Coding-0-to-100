#Madlibs Game
print("Welcome to the Madlibs Game!")
print("Please provide the following inputs to create your story.")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")

story = f"Once upon a time, there was a {adjective} {noun} who loved to {verb}. " \
        f"Every day, {noun} would {verb} around the forest, spreading joy and laughter."
print("Here is your story:")
print(story)
print("Thank you for playing the Madlibs Game!")
# This code creates a simple Madlibs game where the user inputs words to fill in a storytemplate.