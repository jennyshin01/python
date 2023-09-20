#거북이 그래픽으로 그림 그리기
#정오각형을 그리는 프로그램
import turtle as t

n = 5
t.color("purple") #거북이 색상 보라색
t.begin_fill() #채우기 (전)
#색칠할 영역
for x in range(n):
    #반복문 작성 n에 대한
    t.fd(50)
    t.lt(360/n) #왼쪽으로 각도
t.end_fill() #채우기 (완)