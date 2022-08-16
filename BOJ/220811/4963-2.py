import sys
sys.stdin = open("4963.txt")

octagon = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
       break

    matrix = [list(map(int,input().split())) for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if matrix[i][j]:
                stack = [(i,j)]
                matrix[i][j] = False
                cnt += 1

                while stack:
                    x,y = stack.pop()
                    for r,c in octagon:
                        dx = x + r
                        dy = y + c
                        if h > dx >= 0 and w > dy >= 0 and matrix[dx][dy]:
                            stack.append((dx, dy))
                            matrix[dx][dy] = False

    print(cnt)