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
def dfs(i, j, is_block, cnt_flag):
    global answer
    visited[i][j] = True
    if cnt_flag:
        answer += cnt[i][j] if is_block else -cnt[i][j]
    for di, dj in delta:
        ni, nj = i + di, j + dj
        if ni < 0 or nj < 0 or ni >= 102 or nj >= 102: continue
        if board[ni][nj] != is_block or visited[ni][nj]: continue
        dfs(ni, nj, is_block, cnt_flag)

# [Main] 
if __name__ == "__main__":
    # [1] 데이터 입력
    N = int(input())
    blocks = [tuple(map(int, input().split())) for _ in range(N)]
    
    # [2] 블럭 놓기
    board = [[False] * 102 for _ in range(102)]
    for i, j in blocks:
        board[i][j] = True

    # [3] 인접 블록이 몇개인지 카운트
    cnt = [[4] * 102 for _ in range(102)]
    delta = ((-1, 0), (1, 0), (0, -1), (0, 1))
    for i in range(1, 101):
        for j in range(1, 101):
            if not board[i][j]: continue
            for di, dj in delta:
                ni, nj = i + di, j + dj
                if ni < 1 or nj < 1 or ni >= 101 or nj >= 101: continue
                if board[i][j] != board[ni][nj]: continue
                cnt[i][j] -= 1

    # [4] 블럭 외부의 빈칸 체크
    visited = [[False] * 102 for _ in range(102)]
    dfs(0, 0, False, False)

    # [5] 블럭의 외곽선 카운트
    answer = 0
    for i, j in blocks:
        if visited[i][j]: continue
        dfs(i, j, True, True)

    # [6] 블럭 내부 빈칸 체크
    for i in range(102):
        for j in range(102):
            if visited[i][j]: continue
            dfs(i, j, False, True)
    
    # [6] 출력
    print(answer)