import sys
i_n, i_m = map(int, sys.stdin.readline().split())
dct_pokemon = {}
for i_1 in range(1, i_n+1):
    dct_pokemon[i_1] = sys.stdin.readline().rstrip()
dct_pokemon_reverse = {val_1: key_1 for key_1, val_1 in dct_pokemon.items()}

for i_2 in range(i_m):
    s_input = sys.stdin.readline().rstrip()
    if s_input.isdecimal():
        print(dct_pokemon[int(s_input)])
    else:
        print(dct_pokemon_reverse[s_input])