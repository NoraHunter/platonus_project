import difflib

def answers_similarity(ans1_json, ans2_json) -> bool:
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
    return True   