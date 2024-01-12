'''
알파벳 쟁탈전 - 코드트리 실버2
분류 : 백트랙킹
'''
import sys

# [A] 입력함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] 백트랙킹 함수
def dfs(idx):
    global answer
    if idx > N:
        answer += 1
        return
    
    if students[idx] >= 0:
        dfs(idx + 1)
    else:
        rules = []
        for c, a, b in orders:
            if a == idx:
                rules.append((b, cnd[c]))
            elif b == idx:
                rules.append((a, cnd[c]))

        for a in range(3):
            if not possible[idx][a]: continue
            students[idx] = a
            for b, c in rules:
                if c:
                    for k in range(3):
                        if a == k: continue
                        possible[b][k] = False
                else:
                    possible[b][a] = False
            dfs(idx + 1)
            students[idx] = -1
            for b, c in rules:
                if c:
                    for k in range(3):
                        if a == k: continue
                        possible[b][k] = True
                else:
                    possible[b][a] = True

# [Main]
if __name__ == "__main__":
    N, K = map(int, input().split())
    orders = []
    for _ in range(K):
        c, a, b = input().split()
        orders.append((c, int(a), int(b)))

    possible = [[True] * 3 for _ in range(N + 1)]
    students = [-1] * (N + 1)

    answer = 0
    cnd = {'S': True, 'D': False}
    dfs(1)

    print(answer)