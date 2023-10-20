# 6054 : [기초-논리연산] 둘 다 참일 경우만 참 출력하기(설명)(py)

# 2개의 정수값이 입력될 때,
# 그 불 값이 모두 True 일 때에만 True 를 출력하는 프로그램을 작성해보자.
# 예시
# a, b = input().split()
# print(bool(int(a)) and bool(int(b)))
# 참고
# and 예약어는 주어진 두 불 값이 모두 True 일 때에만 True 로 계산하고, 나머지 경우는 False 로 계산한다.
# 이러한 논리연산을 AND 연산(boolean AND)이라고도 부르고, · 으로 표시하거나 생략하며, 집합 기호 ∩(교집합, intersection)로 표시하기도 한다. 
# 모두 같은 의미이다.
# 참, 거짓의 논리값 인 불(boolean) 값을 다루어주는 예약어는 not, and, or 이 있고,
# 불 값들 사이의 논리(not, and, or) 연산 결과도 마찬가지로 True 또는 False 의 불 값으로 계산된다.
# ** 불 대수(boolean algebra)는 수학자 불이 만들어낸 것으로 True(참)/False(거짓) 값만 가지는 논리값과 그 값들 사이의 연산을 다룬다.
# 입력
# 2개의 정수가 공백을 두고 입력된다.
# 출력
# 둘 다 True 일 경우에만 True 를 출력하고, 그 외의 경우에는 False 를 출력한다.

a, b = map(int, input().split())

print(bool(a) and bool(b))