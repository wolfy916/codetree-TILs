'''
블럭의 총 둘레 - 코드트리 골드4
분류 : ?
'''
import sys

# [A] 입력함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [Main] 
if __name__ == "__main__":
    # [1] 데이터 입력
    N = int(input())
    blocks = [tuple(map(int, input().split())) for _ in range(N)]

    # [2] 데이터 초기화
    board = [[False] * 101 for _ in range(101)]
    delta = ((-1, 0), (1, 0), (0, -1), (0, 1))
    cnt = 0
    
    # [3] 블럭 놓기
    for r, c in blocks:
        board[r][c] = True

    # [4] row 기준 탐색
    for r in range(1, 101):
        if True in board[r]:
            cnt += 2
    
    # [5] col 기준 탐색
    for c in range(1, 101):
        if True in map(lambda x: x[c], board):
            cnt += 2
    
    # [6] 출력
    print(cnt)