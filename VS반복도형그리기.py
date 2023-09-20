#반복기능으로 도형을 그리는 프로그램
import turtle as t

#삼각형 그리기
for x in range(3):
    t.fd(100)
    t.lt(120)

#사각형 그리기
for x in range(4):
    t.fd(100) #선
    t.lt(90) #각도

#원 그리기
t.circle(50) #반지름 기준