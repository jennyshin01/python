#선 반복해서 그리기
import turtle as t

angle = 89 #거북이 각도 89
t.bgcolor("black")
t.color("yellow")
t.speed(0) #스피드는 가장 빠르게가 0

for x in range(200): #반복문임!
    t.fd(x) #x값을 0부터 199까지 앞으로?
    t.lt(angle)
