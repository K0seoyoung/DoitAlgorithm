# 구간 합 구하기2
# N*N 크기의 표가 채워져 있다. (x1,y1)에서 (x2,y2)까지의 합 구하기.

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
A = [[0]*(n+1)]                     #원본리스트
D = [[0]*(n+1) for _ in range(n+1)] #합 배열

#원본 리스트 데이터 저장
for i in range(n):
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)

#합 배열 저장
for i in range(1, n+1):
    for j in range(1, n+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]

#구간 합 배열 : 질의답변
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y2-1] + D[x1-1][y1-1]
    print(result)