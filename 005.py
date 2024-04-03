# N개의 수가 주어졌을 때 연속된 부분의 합이 M으로 나누어떨어지는 구간의 개수를 구하는 프로그램을 작성하시오.
# 입력: 1번째 줄에 n과 m(1<=n<=106,2<=m<=103), 2번쩨 줄에서 n개의 수가 주어진다.
# 출력: 1번째 줄에 연속된 부분의 합이 m으로 나누어떨어지는 구간의 개수

import sys
input = sys.stdin.readline
n,m = map(int, input().split())
A = list(map(int, input().split()))
S = [0] * n
C = [0] * m #같은 나머지의 인덱스를 카운트하는 리스트 ????
S[0] = A[0] #why????
answer = 0

#합 배열 저장
for i in range(1,n):
    S[i] = S[i-1] + A[i]

for i in range(n):
    remainder = S[i] % m    #합 배열의 모든 값에 % 연산 수행
    if remainder == 0:      #0~i까지의 구간 합 자체가 0일 때 더하기
        answer += 1         
    C[remainder] += 1       #나머지가 같은 인덱스의 개수 값 증가시키기

for i in range(m):          #나머지가 같은 인덱스 중 2개를 뽑는 경우의 수를 더하기
    if C[i] > 1:
        answer += (C[i] * (C[i]-1) // 2) #int형태

print(answer)