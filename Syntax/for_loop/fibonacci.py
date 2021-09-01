### 피보나치 수열을 원하는 개수만큼 구하기 ###
import numpy as np

fibonacci = np.array([0, 1]) ### 0, 1은 확정
## array([0, 1])객체를 생성한다.

number = int(input('원하는 개수를 입력하세요 (정수 권장) :'))

for i in range(number - 2): ### 2를 빼는 이유는 0, 1은 확정되기 때문이다.
    fibonacci = np.append(fibonacci, fibonacci[-2] + fibonacci[-1])

for i in range(len(fibonacci)):
    print(f'피보나치 {i+1}번째 숫자는 : {fibonacci[i]}입니다.')