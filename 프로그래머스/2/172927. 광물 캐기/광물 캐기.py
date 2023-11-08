# 광물 배치를 5개씩 끊어서
# 다이아몬드 철 돌이 많은 순으로 정렬
# 정렬된 것을 다이아몬드 철 돌 곡괭이 순으로 처리하면 됨 
# 5개 이하를 캘 경우 무조건 효율 다이아 > 철 > 돌이기 때문에 성립
# 조건이 복잡해지면 bfs로 풀어도 될듯
def solution(picks, minerals):
    answer = 0
    # 광물 배치 5개씩 끊어서 개수 세기, 주어진 곡괭이로 캘 수 있는 최대치 도달 시 종료
    index_minerals = 0
    L_minerals = len(minerals)
    max_minerals = sum(picks) * 5
    minerals_5div = []
    cnt_diamond = 0
    cnt_iron = 0
    cnt_stone = 0
    while True:
        if minerals[index_minerals] == "diamond":
            cnt_diamond += 1
            index_minerals += 1
        elif minerals[index_minerals] == "iron":
            cnt_iron += 1
            index_minerals += 1
        elif minerals[index_minerals] == "stone":
            cnt_stone += 1
            index_minerals += 1
        if index_minerals % 5 == 0:
            minerals_5div.append([cnt_diamond, cnt_iron, cnt_stone])
            cnt_diamond = 0
            cnt_iron = 0
            cnt_stone = 0
        if index_minerals == L_minerals or index_minerals == max_minerals:
            minerals_5div.append([cnt_diamond, cnt_iron, cnt_stone])
            break
    # 다이아몬드 철 돌이 많은 순으로 정렬
    minerals_5div.sort()
    # 광물 캐기
    while minerals_5div:
        minerals_inprocess = minerals_5div.pop()
        if picks[0] > 0:
            answer += minerals_inprocess[0] + minerals_inprocess[1] + minerals_inprocess[2]
            picks[0] -= 1
        else:
            if picks[1] > 0:
                answer += 5*minerals_inprocess[0] + minerals_inprocess[1] + minerals_inprocess[2]
                picks[1] -= 1
            else:
                if picks[2] > 0:
                    answer += 25*minerals_inprocess[0] + 5*minerals_inprocess[1] + minerals_inprocess[2]
                    picks[2] -= 1
                else:
                    break

    return answer