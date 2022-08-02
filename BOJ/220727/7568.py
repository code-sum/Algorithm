# 첫 줄에 전체 사람의 수 N이 주어짐
N = int(input())

# 덩치 등수를 담을 리스트 컨테이너 생성
result = []

# 각 학생에 대한 정보를 담을 리스트 컨테이너 생성
data = []

# 그리고 이어지는 N개의 줄에 각 사람의 몸무게, 키를
# 나타내는 양의 정수 x, y가 하나의 공백을 두고 각각 나타남

# Step 1.
for i in range(N):
    x, y = map(int, input().split())
    data.append((x, y))    # data.append(x, y) 아님에 유의!
    # print(data)

# Step 2.
for i in range(N):
    count = 0
    for j in range(N):    # i번째 학생과 j 학생의 [몸무게 and 키] 모두를 비교!
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            count += 1          # i번째 학생보다 j번째 학생이 덩치크면 count + 1 !
                                # i번째 학생보다 덩치 큰 j번째 학생들이 많으면 그만큼 count +1 횟수도 증가
    result.append(count + 1)    # 덩치 등수(0+1+1...)들을 result 리스트에 append

for k in result:
    print(k, end = " ")   # 학생 N명의 덩치 등수를 '공백 문자로 분리해서' 출력