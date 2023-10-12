# [골드III] 자료구조_구간 합_10986_나머지 합 구하기

# 문제
# 수 N개 A1, A2, ..., AN이 주어진다. 이때, 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 구하는 프로그램을 작성하시오.
# 즉, Ai + ... + Aj (i ≤ j) 의 합이 M으로 나누어 떨어지는 (i, j) 쌍의 개수를 구해야 한다.
# 입력
# 첫째 줄에 N과 M이 주어진다. (1 ≤ N ≤ 106, 2 ≤ M ≤ 103)
# 둘째 줄에 N개의 수 A1, A2, ..., AN이 주어진다. (0 ≤ Ai ≤ 109)
# 출력
# 첫째 줄에 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 출력한다.

n, m = map(int, input().split())

A = list(map(int, input().split()))

S = [0] * n
S[0] = A[0]
for i in range(1, n):
    S[i] = S[i-1] + A[i]

C = [0] * m
answer = 0
for i in range(n):
    remain = S[i] % m
    if remain == 0:
        answer += 1
    C[remain] += 1

for i in range(m):
    if C[i] > 1:
        answer += (C[i] * (C[i] - 1)) // 2

print(answer)