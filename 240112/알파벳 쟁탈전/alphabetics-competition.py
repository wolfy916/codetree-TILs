'''
알파벳 쟁탈전 - 코드트리 실버2
분류 : 백트랙킹
'''
import sys
from copy import deepcopy


# [A] 입력함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] 백트랙킹 함수
def dfs(idx):
    global answer, possible
    if idx > N:
        answer += 1
        return
    
    for v in range(3):
        if not possible[idx][v]: continue
        tmp = deepcopy(possible)
        for k in range(3):
                if v == k: continue
                possible[idx][k] = False
        for s in rules[idx][1]:
            for k in range(3):
                if v == k: continue
                possible[s][k] = False
        for d in rules[idx][0]:
            possible[d][v] = False
        dfs(idx + 1)
        possible = tmp

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