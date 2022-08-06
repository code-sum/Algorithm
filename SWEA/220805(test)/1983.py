grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

T = int(input())
for test_case in range(1, T + 1):

    # 테스트 케이스의 첫 번째 줄은 학생수 N 과, 학점을 알고싶은 학생의 번호 K
    N, K = map(int, input().split())

    # 학생 개개인의 total_score 담을 빈 리스트 생성
    list_ = []

    # 테스트 케이스 두 번째 줄 부터 각각의 학생이 받은 시험 및 과제 점수가 주어진다.
    for i in range(N):
        mid, fin, assi = map(int, input().split())
        total_score = (mid * 0.35) + (fin * 0.45) + (assi * 0.2)
        list_.append(total_score)

    # K번째 학생의 total_score 탐색
    K_total_score = list_[K-1]

    # letter grade 가 내림차순으로 정렬되어 있으니,
    # 학생들의 점수를 grade 에 매칭하기 전에 미리 내림차순 정리
    list_.sort(reverse = True)

    # 각 letter grade 마다 배정되는 학생수를 grade_value 에 저장
    grade_value = N // 10

    # 출력하려는 값 = K번째 학생 총점 인덱스를 letter grade 별 학생수로 나누기
    result = list_.index(K_total_score) // grade_value

    # 테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.
    print('#%d %s' % (test_case, grade[result]))