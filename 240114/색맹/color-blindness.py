'''
색맹 - 코드트리 실버1
분류 : 완전 탐색
'''
import sys
from collections import deque as dq

# [A] 입력함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [Main]
if __name__ == "__main__":
    # [1] 데이터 입력 및 초기화
    N = int(input())
    board = [input() for _ in range(N)]
    total_cnt = RG_cnt = 0
    nxt = {'R': ['R', 'G'], 'G': ['R', 'G'], 'B': ['B']}
    visited = [[False] * N for _ in range(N)]
    delta = ((-1, 0), (1, 0), (0, -1), (0, 1))

    # [2] bfs 탐색
    for i in range(N):
        for j in range(N):
            if visited[i][j]: continue
            visited[i][j] = True
            color = {'R': False, 'G': False, 'B': False}
            color[board[i][j]] = True
            queue = dq([(i, j)])
            while queue:
                vi, vj = queue.popleft()
                for di, dj in delta:
                    ni, nj = vi + di, vj + dj
                    if ni < 0 or nj < 0 or ni >= N or nj >= N: continue
                    if visited[ni][nj]: continue
                    if board[ni][nj] not in nxt[board[i][j]]: continue
                    color[board[ni][nj]] = True
                    visited[ni][nj] = True
                    queue.append((ni, nj))
            
            # 그룹 카운트
            total_cnt += list(color.values()).count(True)
            if color['R'] or color['G']: RG_cnt += 1
            if color['B']: RG_cnt += 1
    
    print(total_cnt, RG_cnt)