'''
색맹 - 코드트리 실버1
분류 : 완전 탐색
'''
import sys
from collections import deque as dq

# [A] 입력함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] bfs
def bfs(i, j):
    global RG_cnt
    visited[i][j] = num[board[i][j]]
    queue = dq([(i, j)])
    RG_flag = False
    while queue:
        vi, vj = queue.popleft()
        for di, dj in delta:
            ni, nj = vi + di, vj + dj
            if ni < 0 or nj < 0 or ni >= N or nj >= N: continue
            if board[ni][nj] != board[i][j]:
                if visited[ni][nj] > 1:
                    RG_flag = True
                continue
            if visited[ni][nj]: continue
            visited[ni][nj] = num[board[i][j]]
            queue.append((ni, nj))
    if RG_flag and board[i][j] != 'B':
        RG_cnt -= 1

# [Main]
if __name__ == "__main__":
    # [1] 데이터 입력 및 초기화
    N = int(input())
    board = [input() for _ in range(N)]
    total_cnt = RG_cnt = 0
    num = {'R': 3, 'G': 2, 'B': 1}
    visited = [[0] * N for _ in range(N)]
    delta = ((-1, 0), (1, 0), (0, -1), (0, 1))

    # [2] bfs 탐색
    for i in range(N):
        for j in range(N):
            if visited[i][j]: continue
            total_cnt += 1
            RG_cnt += 1
            bfs(i, j)
    
    print(total_cnt, RG_cnt)