#함수응용하기
#1부터 n까지의 합을 구하는 함수
def sum_func(n):
    s = 0
    for x in range(1,n+1):
        s = s + x
    return s

#위에 문장들이 식 생성하기

print(sum_func(10))
print(sum_func(100))
