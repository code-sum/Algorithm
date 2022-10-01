import sys
sys.stdin = open("1288_input.txt", "r")

T = int(input())

for test_case in range(1, T+1) :
    N = int(input())

    listA = [0]*10

    i = 0
    while(True) :
        if 0 not in listA :
            break
        else :
            i += 1
            num = str(N*i)
            for j in range(len(num)) :
                listA[int(num[j])] = 1


    print("#{} {}".format(test_case, num))