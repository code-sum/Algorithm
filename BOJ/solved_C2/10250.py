# https://www.acmicpc.net/problem/10250


t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())

    # n번째 손님에게 배정되어야하는 방번호 출력
    # result = str(층수 floor) + str(층별방번호 num) 

    floor = n % h 
    room_number = (n // h) + 1

    if floor == 0:
        floor = h
        room_number -= 1
    
    print(floor * 100 + room_number)