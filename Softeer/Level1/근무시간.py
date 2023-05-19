# https://softeer.ai/practice/info.do?idx=1&eid=990

import sys

# 해당 직원이 일주일동안 근무한 총 시간을 분단위로 출력

time = []

for _ in range(5):
    start, end = list(map(str, input().split(" ")))

    start_time = int(start[:2])
    start_minute = int(start[3:])

    end_time = int(end[:2])
    end_minute = int(end[3:])

    minute_dif = end_minute - start_minute
    time_dif = end_time - start_time

    if minute_dif >= 0:
        time.append((time_dif*60) + minute_dif)
    else:
        time.append((((time_dif)-1)*60) + (60+(minute_dif)))
    
print(sum(time))