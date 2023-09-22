#결과값이 있는 함수
def square(a):
    c = a * a
    return c
#a제곱을 구하는 함수 = 정사각형의 넓이를 구함
def triangle(a,h):
    c = a * h /2
    return c
#밑변이 a고 높이가 h인 삼각형의 넓이를 구하는 공식

s1 = 4
s2 = square(s1)
print(s1,s2)

print(triangle(3,4))