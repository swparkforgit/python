# HTML태그를 출력하는 함수
def p(content):
    return "<p class=\"line-up\">{}</p>".format(content)

print(p("안녕하세요"))