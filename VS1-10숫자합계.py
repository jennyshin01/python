#1부터 10까지 숫자의 합계를 구하는 프로그램
s = 0
for x in range(1, 10+1): #합계를 구하는 변수 s, 처음값은 0
    s = s+x #현재의 x값에 s값을 더함
    print("x:", x," sum:", s) #print값 안에 x값과, s값을 출력함