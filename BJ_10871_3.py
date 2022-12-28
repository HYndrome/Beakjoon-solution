a, b = map(int, input().split())
score = [score for score in input().split if int(score) < b]
print(" ".join(score))