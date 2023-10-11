# [실버III] 자료구조_구간 합_11659_구간 합 구하기 1

# 문제: [브론즈I] 자료구조_배열과 리스트_1546_평균 구하기
# 입력: 첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다. 둘째 줄에는 N개의 수가 주어진다. 수는 1,000보다 작거나 같은 자연수이다. 셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.
# 출력: 총 M개의 줄에 입력으로 주어진 i번째 수부터 j번째 수까지 합을 출력한다.

dataNo, quizNo = map(int , input().split())

numbers = list(map(int, input().split()))

prefix_sum = [0]

temp = 0
for i in numbers:
    temp += int(i)
    prefix_sum.append(temp)

for i in range(quizNo):
    s, e = map(int, input().split())
    print(prefix_sum[e] - prefix_sum[s-1])


