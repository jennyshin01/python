#다각형을 그리는 함수
import turtle as t
def polygon(n):
    for x in range(n): #n번 반복
        t.fd(50) #앞으로 50감
        t.lt(360/n) #각도는 왼쪽으로 360/n만큼 돎

def polygon2(n,a):
    for x in range(n):
        t.fd(a)
        t.lt(360/n)
polygon(3) #삼각형
polygon(5) #오각형

#그림을 안그리고 거북이를 이동
t.up()
t.fd(100)
t.down()

polygon2(3,75)
polygon2(5,100)