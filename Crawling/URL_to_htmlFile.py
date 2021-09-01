### URL을 입력하면 해당 페이지의 html 소스코드를 자동으로 파일화 하는 프로그램 ### 
# 필요 패키지 requests, bs4.BeautifulSoup, lxml

# 1. 패키지 불러오기
import requests ### 패키지가 없다면 pip install requests && pip list | grep requests 명령어로 설치 및 확인
from bs4 import BeautifulSoup



url = input('URL을 입력하세요 :')


res = requests.get(url) ### 입력받은 URL로 response 객체를 생성합니다.
res.raise_for_status()
## 해당 페이지를 못 찾았을 시엔 예외를 발생시켜 종료

soup = BeautifulSoup(res.text, 'lxml')
## response 객체를 bs로 파싱

#
title = soup.title.get_text()
print(title)

with open(f'{title}.html', 'w', encoding='utf-8') as file:
    file.write(res.text)
    ## html 코드를 그대로 파일화하기 저장위치는 파일과 같은 디렉토리