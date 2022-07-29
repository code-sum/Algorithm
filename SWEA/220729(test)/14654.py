# 신용카드 만들기2

n = int(input())

for _ in range(1, n+1):

    # 입력된 카드번호 중에 '-' 기호가 들어있으면 제거하고 연산
    # 인덱스를 쉽게 비교하기 위해 입력된 카드번호(str)를 리스트로 형 변환
    data = input()
    new_data = data.replace('-', '')
    list_new_data = list(new_data)

    for i in list_new_data:

        # 첫번째 제약조건
        if list_new_data[0] != '3' and list_new_data[0] != '4' and list_new_data[0] != '5' and list_new_data[0] != '6' and list_new_data[0] != '9':
            print(f'#{_} 0')
            break
        else:

            # 두번째 제약조건
            if len(list_new_data) == 16:
                print(f'#{_} 1')
                break
            else:
                print(f'#{_} 0')
                break