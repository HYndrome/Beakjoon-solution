def solution(s):
    answer = True
    ls_bracket = []
    for s_1 in s:
        if s_1 == "(":
            ls_bracket.append("(")
        elif s_1 == ")":
            if not ls_bracket:
                return False
            ls_bracket.pop()
    if not ls_bracket:
        return True
    else:
        return False