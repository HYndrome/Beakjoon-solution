import sys
while True:
    s_input = sys.stdin.readline().rstrip()
    if s_input == '.':
        break
    stack_bracket = []
    for s_1 in s_input:
        if s_1 == '(':
            stack_bracket.append('(')
        elif s_1 == '[':
            stack_bracket.append('[')
        elif s_1 == ')':
            try:
                if stack_bracket[-1] == '(':
                    stack_bracket.pop()
                else:
                    print('no')
                    break
            except:
                print('no')
                break
        elif s_1 == ']':
            try:
                if stack_bracket[-1] == '[':
                    stack_bracket.pop()
                else:
                    print('no')
                    break
            except:
                print('no')
                break
    else:
        if not stack_bracket:
            print('yes')
        else:
            print('no')
