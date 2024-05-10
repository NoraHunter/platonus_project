import json, difflib, random, pprint

def get_similar_question(question : str, questions: dict) -> dict:
    similar_question_key = ""
    high_ratio = 0.0
    for key in questions.keys():
        curr_ratio = difflib.SequenceMatcher(None, question, questions[key]["question"]).ratio()
        if curr_ratio > high_ratio:
            similar_question_key = key
            high_ratio = curr_ratio
    print(f"High ration is : {high_ratio}")
    return questions[similar_question_key]