n = int(input())

for i in range(1, n + 1) :
    if len(str(i)) < 2 :
        if i in [3, 6, 9] :
            print('-', end=' ')
        else :
            print(i, end=' ')
    else :
        value = ''
        for j in range(len(str(i))) :
            if int(str(i)[j]) == 3 or int(str(i)[j]) == 6 or int(str(i)[j]) == 9 :
                value += '-'

        if len(value) >= 1 :
            print(value, end=' ')
        else :
            print(i, end=' ')