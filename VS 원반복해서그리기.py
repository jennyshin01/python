#원을 반복해서 그리는 프로그램

import turtle as t

n = 50 #몇 개 그릴지
t.bgcolor("black") #배경화면 검정

t.color("green") #색상은 초록

t.speed(0) #거북이속도 가장빠름


for x in range(n):

    t.circle(50)

    t.lt(360/n)