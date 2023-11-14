from collections import deque

def solution(m, n, startX, startY, balls):
    answer = []
    que_ball = deque(balls)
    INF = int(1e9)
    while que_ball:
        targetX, targetY  = que_ball.popleft()

        distanceUp = INF
        distanceDown = INF
        distanceLeft = INF
        distanceRight = INF
        # 윗벽 x 값이 같을 때 startY > targetY
        if startX != targetX or startY > targetY:
            distanceUp = (startX - targetX)**2 + ((n - startY) + (n - targetY))**2
        # 아랫벽 x 값이 같을 때, startY < targetY
        if startX != targetX or startY < targetY:
            distanceDown = (startX - targetX)**2 + (startY + targetY)**2
        # 왼벽 y 값이 같을 때, startX < targetX
        if startY != targetY or startX < targetX:
            distanceLeft = (startX + targetX)**2 + (startY - targetY)**2
        # 오른벽 y 값이 같을 때, startX > targetX
        if startY != targetY or startX > targetX:
            distanceRight = ((m - startX) + (m - targetX))**2 + (startY - targetY)**2
        # print(distanceUp, distanceDown, distanceLeft, distanceRight)
        distanceCurrent = min(distanceUp, distanceDown, distanceLeft, distanceRight)
        answer.append(distanceCurrent)


    return answer