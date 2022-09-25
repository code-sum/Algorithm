import sys
sys.stdin = open("2056.txt")

T = int(input())

days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

for i in range(1, T+1):
    input_ = str(input())
    y = input_[0:4]
    m = input_[4:6]
    d = input_[6:8]
   
    ans = ''
    if 0 < int(m) < 13 and 0 < int(d) <= days[int(m)]:
        ans = y + '/' + m + '/' + d
    else:
        ans += '-1'
       
    print("#" + str(i) + " " + ans)