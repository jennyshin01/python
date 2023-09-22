#while사용하기 유용할 때
#숫자를 추측해서 맞추는 프로그램
import random
n=random.randint(1,30)
#1부터 30까지 랜덤한 정수int를 뽑을것임 누가? n이
while True:
    #영원히 반복함
    x = input("맞혀보세요?")
    g = int(x)
    if g == n:
        print("정답!")
        break
    if g<n:
        print("너무 작아요.")
    if g>n:
        print("너무 커요.")