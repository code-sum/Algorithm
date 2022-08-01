# 첫째 줄에 상근이가 측정한 높이이자 수열의 크기 N(=측정 구간 번호) input
N = int(input())
# 둘째 줄에 N개의 양의 정수(=실제 구간별 측정 높이들) input
height = list(map(int,(input().split())))

ascent = []        # 출력하려는 값: 오르막길의 크기 ---- []에 담아놓기
temp = height[0]   # 맨 처음 측정한 길 높이를 임시변수 temp 에 넣음
sum = 0            # 오르막길 높이의 최종 증가분(반복문 시작 전이니까 0으로 초기화)

for i in range(1, N):
    if height[i] - temp > 0:       # 길 높이가 이전보다 커질 때마다,
        sum += height[i] - temp    # 커진 만큼의 값을 sum 에 더해줌
        temp = height[i]           # temp 는 회차가 반복될 때마다 height[0] ~ height[N-1]까지 업데이트
        
    elif height[i] == temp or height[i]-temp < 0:     # 길 높이가 이전과 같거나(평지), 이전보다 작아지면,
        ascent.append(sum)         # 오르막길이 아니므로 이전까지의 sum 값을 비어있던 리스트(ascent)에 추가
        temp = height[i]           # temp 는 회차가 반복될 때마다 height[0] ~ height[N-1]까지 업데이트(오르막때와 마찬가지)
        sum = 0        # ascent 라는 리스트에 sum 값을 붙여넣어주고 있으므로, 
                       # 평지&내리막길에 해당하는 조건문 내에서 sum 값은 초기화 시키며 마무리
ascent.append(sum)     # 만약 마지막으로 측정한 높이가 이전보다 높아진 오르막이라면, 
                       # 위에서 작성한 for문으로는 붙여줄 수 없으니(다음 단계가 내리막이어야 sum 을 ascent에 붙여주도록 코드 작성)
                       # append 명령어를 별도로 추가
if len(ascent) == 0:
    print(0)            # 만약 오르막길이 없으면 0을 출력
else: 
    print(max(ascent))  # 그렇지 않으면, 첫째 줄에 가장 큰 오르막길의 크기를 출력