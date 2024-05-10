import json
import difflib
import random
import pprint

'''
template
"test_id-" + "id" : {
        "question" : "",
        "answers" : {
            "c_ans-0" : "",
            "w_ans-0" : "",
            "w_ans-1" : "",
            "w_ans-2" : "",
            "w_ans-3" : "",
            "w_ans-4" : "",
        }
    },
'''

with open("tests.json", 'r', encoding="utf-8") as file:
    tests = json.loads(file.read())
# KEY MACROS
QUESTION = "question"
ANSWERS = "answers"
#pprint.PrettyPrinter(indent=4)
#print(type(tests))
#pprint.pprint(tests)

'''def answers_similarity(ans1_json, ans2_json) -> bool:
    ans1 = list(ans1_json)
    ans2 = list(ans2_json)
    if len(ans1) != len(ans2):
        return False
    for i in range(len(ans1)):
        rm_i = None
        for j in range(len(ans2)):
           if difflib.SequenceMatcher(None, ans1[i], ans2[j]).ratio() >= 0.80:
             rm_i = j
             break
        if rm_i is None:
           return False
        del ans2[rm_i]
    return True   '''

def get_similar_test(ques : str) -> dict:
    similar_test_id = ""
    high_ratio = 0.0
    for key in tests.keys():
        curr_ratio = difflib.SequenceMatcher(None, ques, tests[key]["question"]).ratio()
        if difflib.SequenceMatcher(None, ques, tests[key]["question"]).ratio() > high_ratio:
            similar_ques = key
            high_ratio = curr_ratio
    return tests[key]

tests = list(tests.values())
random.shuffle(tests)
for test in tests:
    print(test[QUESTION])
    answers = list(test[ANSWERS].values())
    random.shuffle(answers)
    for index, answer in enumerate(answers):
        print(f"{index + 1}) {answer}")
    correct_ans_keys = [e for e in test[ANSWERS].keys() if "c_ans" in e]
    print(correct_ans_keys)
    user_ans = []
    for u_ans_i in range(len(correct_ans_keys)):
        user_ans.append(
            int(input(f"User answer #{u_ans_i + 1} : "))   -   1
        )
    
    user_correct_count = 0
    for key in correct_ans_keys:
        if 
    

