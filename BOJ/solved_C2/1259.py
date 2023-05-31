# https://www.acmicpc.net/problem/1259

while True:
    num_list = list(map(str, input()))

    if num_list == ['0']:
        break

    if num_list == num_list[::-1]:
        print('yes')
    else:
        print('no')