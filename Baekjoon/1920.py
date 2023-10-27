# [실버IV]
# 1920_수 찾기

# 문제
# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -2^31 보다 크거나 같고 2^31보다 작다.

# 출력
# M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.

print('입력')
data_num = int(input()) # 5
data_ls = list(map(int, input().split())) # 4, 1, 5, 2, 3

data_ls.sort() # 데이터 리스트 정렬

target_num = int(input()) #5
target_ls = list(map(int, input().split())) # 1, 3, 7, 9, 5

print()
print('출력')

for i in range(target_num):
    target = target_ls[i] # 찾으려는 값

    start = 0 # 시작 인덱스
    end = len(target_ls) - 1 # 종료 인덱스
    
    result = []
    while start <= end: # 시작 인덱스가 종료 인덱스보다 작거나 같을 때만 반복
        mid = int((start + end) / 2) # 중앙 인덱스
        median = data_ls[mid] # 중앙값
        
        if target < median: # 찾으려는 값이 중앙값보다 작으면 왼쪽 부분 탐색
            end = mid - 1
            
        elif target > median: # 찾으려는 값이 중앙값보다 크면 오른쪽 부분 탐색
            start = mid + 1

        else:
            result.append('search') # 찾으려는 값과 중앙값이 같으면 결과 리스트에 '탐색' 추가하고 탐색 종료
            break

    if 'search' in result: # 결과 리스트에 '탐색'이 있으면 '1' 출력
        print(1)
    else:  # 결과 리스트에 '탐색'이 없으면 '0' 출력
        print(0)