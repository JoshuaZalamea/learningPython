def get_questions():
    return [["What is the name of Josh's dog? ", "Sadie"],
            ["What is 2+2? ", "4"],
            ["What's at the edge of the ocean? ","beach"]]

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

run_test(get_questions())