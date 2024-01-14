'''
색맹 - 코드트리 실버1
분류 : 구현, 완전 탐색
'''
import sys
from collections import deque as dq

# [A] 입력함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] bfs
def bfs(i, j, flag):
    visited[i][j] = 0 if flag else num[board[i][j]]
    queue = dq([(i, j)])
    while queue:
        vi, vj = queue.popleft()
        for di, dj in delta:
            ni, nj = vi + di, vj + dj
            if ni < 0 or nj < 0 or ni >= N or nj >= N: continue
            if flag:
                if board[ni][nj] not in nxt[board[i][j]]: continue
                if not visited[ni][nj]: continue
            else:
                if board[ni][nj] != board[i][j]: continue
                if visited[ni][nj]: continue
            visited[ni][nj] = 0 if flag else num[board[i][j]]
            queue.append((ni, nj))
# [Main]
if __name__ == "__main__":
    # [1] 데이터 입력 및 초기화
    N = int(input())
    board = [input() for _ in range(N)]
    num = {'R': 3, 'G': 2, 'B': 1}
    nxt = {'R': ['R', 'G'], 'G': ['R', 'G'], 'B': ['B']}
    delta = ((-1, 0), (1, 0), (0, -1), (0, 1))

    # [2] 전체 그룹 탐색
    total_cnt = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j]: continue
            total_cnt += 1
            bfs(i, j, False)

    # [3] 색약 그룹 탐색
    RG_cnt = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]: continue
            RG_cnt += 1
            bfs(i, j, True)
    
    print(total_cnt, RG_cnt)