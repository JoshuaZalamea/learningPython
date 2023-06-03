def get_questions():
    return [["What is the name of Josh's dog? ", "Sadie"],
            ["What is 2+2? ", "4"],
            ["What's at the edge of the ocean? ","beach"],
            ["Dogs or cats? ", "dogs"]]

def check_question(question_and_answer):
    question = question_and_answer[0]
    answer = question_and_answer[1]
    given_answer = input(question)
    if answer == given_answer:
        print("Correct")
        return True
    else:
        print("Incorrect, answer was: ", answer)
        return False

def run_test(questions):
    if len(questions) == 0:
        print("No questions were given.")
        return
    index = 0
    right = 0
    while index < len(questions):
        if check_question(questions[index]):
            right = right + 1
        index = index + 1
    print("You got", right * 100 / len(questions),\
            "% right out of", len(questions))

def answer_key(questions):
    index = 0
    while index < len(questions):
        print(" ")
        print(questions[0])
        print(questions[1])
        print(questions[2])
        print(questions[3])
        return

choice = None

while choice != "q":
    print(" ")
    print("Select an option from the following list:")
    print(" 't' for test")
    print(" 'k' for answer key")
    print(" 'q' for quit")
    print(" ")
    choice = input("Enter here: ")
    if choice == "t":
        print(" ")
        run_test(get_questions())
    if choice == "k":
        print(" ")
        answer_key(get_questions())
    if choice == "q":
        print(" ")
        print("Quitting...")
        break