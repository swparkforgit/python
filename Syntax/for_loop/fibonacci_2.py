### 피보나치 수열을 좀더 간단하게 표현한 프로그램 ###

n = int(input("원하는 개수를 입력하세요 : "))

a, b = 0, 1
for i in range(n):
    print(f'{i+1}번째 숫자는 : {a}입니다.')
    a, b = b, a+b