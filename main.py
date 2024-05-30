import json, difflib, random, pprint

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE  = '\033[34m'
ORANGE = '\u001b[38;5;166m'
RESET = '\033[0m'


'''questions.json template
{
    "question_id-id" : {
        "question" : "",
        "answers" : {
            "c_ans-0" : "",
            "c_ans-1" : "",
            ...
            "w_ans-0" : "",
            "w_ans-1" : "",
            "w_ans-2" : "",
            "w_ans-3" : "",
            "w_ans-4" : "",
            ...
        }
    },
    ...
}'''

with open("questions.json", 'r', encoding="utf-8") as file:
    questions = json.loads(file.read())


questions = list(questions.values())
random.shuffle(questions)
for question in questions:
    # Getting all correct answer keys from var:question and prints question
    correct_ans_keys = [e for e in question["answers"].keys() if "c_ans" in e]
    print(f"{BLUE}{question["question"]}{RESET}      -{'*' * len(correct_ans_keys)}-")
    answers = list(question["answers"].values())
    random.shuffle(answers)
    for index, answer in enumerate(answers):
        print(f"{ORANGE}{index + 1}) {answer}{RESET}")
    
    # Getting input from user
    user_answers = []
    input_count = 0
    while input_count < len(correct_ans_keys):
        user_input = int(input(f"User answer #{input_count + 1} : "))   -   1
        if user_input >= len(answers) or user_input < 0:
            continue
        user_answers.append(answers[user_input])
        input_count += 1

    # Checking count of user score
    print(f"{YELLOW}Your answers :    {user_answers}{RESET}")
    print(f"{YELLOW}Correct answers : {  list({k: v for k, v in question["answers"].items() if "c_ans" in k}.values())  }  {RESET}")
    user_correct_count = 0
    for key in correct_ans_keys:
        if question["answers"][key] in user_answers:
            user_correct_count += 1
    print(f"{GREEN}Score : {user_correct_count}/{len(correct_ans_keys)}{RESET}\n\n\n")

    

