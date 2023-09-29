name = input('이름을 입력하세요 : ')
id = input('학번을 입력하세요 : ')
zero = id.count('0')

print("이름 : {} 학번 : {}\n학번에 0은 {}번 나옵니다.".format(name, id, zero))