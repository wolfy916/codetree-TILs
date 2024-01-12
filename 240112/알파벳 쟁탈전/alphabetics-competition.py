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
    
    for v in range(3):
        if not possible[idx][v]: continue
        tmp = []
        for k in range(3):
                if v == k: continue
                if not possible[idx][k]: continue
                tmp.append((idx, k))
                possible[idx][k] = False
        for s in rules[idx][1]:
            for k in range(3):
                if v == k: continue
                if not possible[s][k]: continue
                tmp.append((s, k))
                possible[s][k] = False
        for d in rules[idx][0]:
            if not possible[d][v]: continue
            tmp.append((d, v))
            possible[d][v] = False
        dfs(idx + 1)
        for t1, t2 in tmp:
            possible[t1][t2] = True

# [Main]
if __name__ == "__main__":
    N, K = map(int, input().split())
    cnd = {'S': 1, 'D': 0}
    rules = [[[], []] for _ in range(N + 1)]
    for _ in range(K):
        c, a, b = input().split()
        a, b = int(a), int(b)
        if a > b:
            rules[b][cnd[c]].append(a)
        else:
            rules[a][cnd[c]].append(b)

    possible = [[True] * 3 for _ in range(N + 1)]
    answer = 0
    dfs(1)

    print(answer)