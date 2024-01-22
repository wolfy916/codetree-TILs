'''
블럭의 총 둘레 - 코드트리 골드4
분류 : DFS
'''
import sys
sys.setrecursionlimit(100000)

# [A] 입력함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] dfs
def dfs(i, j):
    global answer
    visited[i][j] = True
    for di, dj in delta:
        ni, nj = i + di, j + dj
        if ni < 0 or nj < 0 or ni >= 102 or nj >= 102: continue
        if visited[ni][nj]: continue
        # 빈 공간에서 블럭을 발견하면 선분 1개 카운트
        if board[ni][nj]:
            answer += 1
        else:
            dfs(ni, nj)

# [Main] 
if __name__ == "__main__":
    # [1] 데이터 입력
    N = int(input())
    blocks = [tuple(map(int, input().split())) for _ in range(N)]
    
    # [2] 블럭 놓기
    board = [[False] * 102 for _ in range(102)]
    for i, j in blocks:
        board[i][j] = True

    # [3] dfs 탐색
    visited = [[False] * 102 for _ in range(102)]
    delta = ((-1, 0), (1, 0), (0, -1), (0, 1))
    answer = 0
    dfs(0, 0)  # 1 ~ 100을 벗어난 위치에서 탐색 시작
    
    # [4] 출력
    print(answer)