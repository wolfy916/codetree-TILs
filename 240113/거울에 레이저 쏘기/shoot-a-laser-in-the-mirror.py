'''
거울에 레이저 쏘기 - 코드트리 실버1
분류 : 2차원 탐색
'''
import sys

# [A] 입력함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] 레이저 반사횟수 카운팅
def count(i, j, prev):
    global answer
    if visited[i][j]: return
    visited[i][j] = True
    cnt = 0
    while 0 <= i < N and 0 <= j < M:
        cnt += 1
        di, dj = link[prev][kind[board[i][j]]]
        i += di
        j += dj
        prev = (di, dj)
    visited[i - di][j - dj] = True
    answer = max(answer, cnt)

# [Main]
if __name__ == "__main__":
    # [1] 데이터 입력 및 초기화
    N, M = map(int, input().split())
    board = [input() for _ in range(N)]
    kind = {'/': 0, '\\': 1}
    delta = ((-1, 0), (1, 0), (0, -1), (0, 1))
    link = {
        (0, 1): ((-1, 0), (1, 0)),
        (0, -1): ((1, 0), (-1, 0)),
        (1, 0): ((0, -1), (0, 1)),
        (-1, 0): ((0, 1), (0, -1))
    }
    visited = [[False] * M for _ in range(N)]
    answer = 0

    # [2] 2차원 배열의 가장자리에서 탐색 시작
    for i in range(N):
        if i < 1 or i >= N - 1:
            for j in range(M):
                dir = 1 if i < 1 else 0
                count(i, j, delta[dir])
        else:
            for j in [0, M - 1]:
                dir = 2 if j > 0 else 3
                count(i, j, delta[dir])

    print(answer)