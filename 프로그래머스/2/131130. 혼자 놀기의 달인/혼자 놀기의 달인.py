def solution(cards):
    set_used = set()
    len_cardset = []
    for card in cards:
        if card not in set_used:
            set_current = set()
            card_current = card
            while card_current not in set_current:
                set_used.add(card_current)
                set_current.add(card_current)
                card_current = cards[card_current-1]
            len_cardset.append(len(set_current))
    len_cardset.sort(key=lambda x: -x )
    if len(len_cardset) == 1:
        answer = 0
    else:
        answer = len_cardset[0] * len_cardset[1]            
    return answer