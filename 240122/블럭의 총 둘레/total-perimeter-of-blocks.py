'''
블럭의 총 둘레 - 코드트리 골드4
분류 : DFS
'''
import sys

# [A] 입력함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] dfs
def dfs(i, j):
    global answer
    visited[i][j] = True
    answer += cnt[i][j]
    for di, dj in delta:
        ni, nj = i + di, j + dj
        if ni < 0 or nj < 0 or ni >= 101 or nj >= 101: continue
        if not board[ni][nj] or visited[ni][nj]: continue
        dfs(ni, nj)

# [Main] 
if __name__ == "__main__":
    # [1] 데이터 입력
    N = int(input())
    blocks = [tuple(map(int, input().split())) for _ in range(N)]
    
    # [2] 블럭 놓기
    board = [[False] * 101 for _ in range(101)]
    for i, j in blocks:
        board[i][j] = True

    # [3] 인접 블록이 몇개인지 카운트
    cnt = [[0] * 101 for _ in range(101)]
    delta = ((-1, 0), (1, 0), (0, -1), (0, 1))
    for i in range(1, 101):
        for j in range(1, 101):
            if not board[i][j]: continue
            for di, dj in delta:
                ni, nj = i + di, j + dj
                if ni < 0 or nj < 0 or ni >= 101 or nj >= 101: continue
                if not board[ni][nj]: continue
                cnt[i][j] += 1

    # [4] dfs 탐색
    visited = [[False] * 101 for _ in range(101)]
    answer = 0
    for i, j in blocks:
        if visited[i][j]: continue
        dfs(i, j)
    
    # [6] 출력
    print(answer)