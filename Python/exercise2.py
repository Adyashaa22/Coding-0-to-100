#2-D List Exercise
fruits = ["apple", "banana", "cherry"]
vegetables = ["carrot", "broccoli", "spinach"]
meats = ["chicken", "turkey", "fish"]

grocery_list = [fruits, vegetables, meats]
print(grocery_list,)
# print("Fruits:")
# for fruit in fruits:
#     print(f"- {fruit:>5}")

# print("Vegetables:")
# for vegetable in vegetables:
#     print(f"- {vegetable:>5}")


#quiz game exercise
questions = ("What is the capital of France?", "What is 2 + 2?", "What is the largest planet in our solar system?","Who wrote 'Romeo and Juliet'?","What is the boiling point of water in Celsius?", "What is the chemical symbol for gold?","What is the square root of 64?","Who painted the Mona Lisa?","What is the currency of Japan?","What is the largest mammal?")
options = (("a) Paris", "b) London", "c) Berlin", "d) Madrid"),
            ("a) 3", "b) 4", "c) 5", "d) 6"),
            ("a) Earth", "b) Jupiter", "c) Saturn", "d) Mars"),
            ("a) Shakespeare", "b) Dickens", "c) Austen", "d) Orwell"),
            ("a) 90", "b) 100", "c) 80", "d) 110"),
            ("a) Au", "b) Ag", "c) Pb", "d) Hg"),
            ("a) 6", "b) 7", "c) 8", "d) 9"),
            ("a) Da Vinci", "b) Picasso", "c) Van Gogh", "d) Monet"),
            ("a) Yen", "b) Dollar", "c) Euro", "d) Pound"),
            ("a) Blue Whale", "b) Elephant", "c) Giraffe", "d) Hippopotamus"))
answers = ("a", "b", "b", "a", "b", "a", "c", "a", "a", "a")
guesses = []
score = 0
question_number = 0
for question in questions:
    print("---------------------------")
    print(question)
    for option in options[question_number]:
        print(option)
    question_number += 1
    guess = input("Enter your answer (a, b, c, or d): ").lower()
    guesses += [guess]
    if guess == answers[question_number-1]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect.")