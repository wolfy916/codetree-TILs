'''
거울에 레이저 쏘기 - 코드트리 실버1
분류 : ?
'''
import sys

# [A] 입력함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] 카운팅 함수
def count(i, j, k):
    global answer
    cnt = 0
    while 0 <= i < N and 0 <= j < M:
        if visited[i][j]: return
        visited[i][j] = True
        cnt += 1
        di, dj = link[delta[k]][kind[board[i][j]]]
        i += di
        j += dj
        k = delta.index((di, dj))
    answer = max(answer, cnt)

# [Main]
if __name__ == "__main__":
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

    answer = 0
    visited = [[False] * M for _ in range(N)]
    for i in range(N):
        if i < 1 or i >= N - 1:
            for j in range(M):
                dir = 1 if i < 1 else 0
                count(i, j, dir)
        else:
            for j in [0, M - 1]:
                dir = 3 if j > 0 else 2
                count(i, j, dir)

    print(answer)