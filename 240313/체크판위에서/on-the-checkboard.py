import sys

def input():
    return sys.stdin.readline().rstrip('\n')

def dfs(vi, vj):
    global answer
    if (vi, vj) == (R - 1, C - 1):
        answer += 1
        return
    for wi in range(vi + 1, R):
        for wj in range(vj + 1, C):
            if board[vi][vj] == board[wi][wj]: continue
            dfs(wi, wj)

if __name__ == "__main__":
    R, C = map(int, input().split())
    board = [input() for _ in range(R)]

    answer = 0
    dfs(0, 0)    

    print(answer)