#1부터 n까지의 곱을 구하는 함수
def factorial(n):
    fact = 1
    #곱을 구하기 위한 변수 fact(시작값을 1로 지정)
    for x in range(1, n+1):
        fact = fact * x
    return fact
    #계산된 fact값을 돌려줌

print(factorial(5))
print(factorial(10))