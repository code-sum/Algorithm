# https://www.acmicpc.net/problem/1063

import sys
sys.stdin = open("1063.txt")

move = {
    "R": (0, 1),
    "L": (0, -1),
    "B": (1, 0),
    "T": (-1, 0),
    "RT": (-1, 1),
    "LT": (-1, -1),
    "RB": (1, 1),
    "LB": (1, -1)
}

king, stone, n = input().split()
king_row, king_col = 8-int(king[1]), ord(king[0])-ord("A")
stone_row, stone_col = 8-int(stone[1]), ord(stone[0])-ord("A")

# input_ 명령에 따라 움직이기
for _ in range(int(n)):
    input_ = input().strip()
    input_row, input_col = move[input_]
    if not (0 <= king_row+input_row < 8 and 0 <= king_col+input_col < 8):
        continue
    king_row += input_row
    king_col += input_col
    if (king_row, king_col) == (stone_row, stone_col):
        if not (0 <= stone_row+input_row < 8 and 0 <= stone_col+input_col < 8):
        	# 킹의 움직임 되돌리기
            king_row -= input_row
            king_col -= input_col
            continue
        stone_row += input_row
        stone_col += input_col
       
print(chr(ord("A")+king_col)+str(8-king_row))
print(chr(ord("A")+stone_col)+str(8-stone_row))