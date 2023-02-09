while True:
    s_input = input()
    if s_input == '0':
        break
    else:
        if s_input == s_input[::-1]:
            print('yes')
        else:
            print('no')