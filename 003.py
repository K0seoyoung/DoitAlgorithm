# 구간 합 구하기 1
# 리스트 원소 개수와 합을 구해야하는 횟수가 주어진다. i번째에서 j번째까지의 합구하기

import sys
input = sys.stdin.readline
arrNo, quizNo = map(int, input().split())
numbers = list(map(int, input().split()))
sumArr = []
temp = 0

for i in numbers:
    temp += i
    sumArr.append(temp)

for i in range(quizNo):
    s, e = map(int, input().split())
    print(sumArr[e+1]-sumArr[s])