def dfs(cnt, cur, check_cnt):
    global answer
    if cnt >= answer: return
    if check_cnt >= n:
        answer = min(answer, cnt)
        return

    for i in range(n):
        if check[i]: continue
        if cur[i] + 1 < target[i]:
            cur[i] += 1
            dfs(cnt + 1, cur, check_cnt)
            cur[i] -= 1
        elif cur[i] + 1 == target[i]:
            cur[i] += 1
            check[i] = True
            dfs(cnt + 1, cur, check_cnt + 1)
            cur[i] -= 1
            check[i] = False
    
    for i in range(n):
        if cur[i] * 2 > target[i]: return
    tmp1 = list(map(lambda x: x * 2, cur))
    tmp2 = 0
    prev = []
    for i in range(n):
        if not check[i] and tmp1[i] == target[i]:
            check[i] = True
            tmp2 += 1
            prev.append(i)
    dfs(cnt + 1, tmp1, check_cnt + tmp2)
    for i in prev:
        check[i] = False


n = int(input())
target = list(map(int, input().split()))
answer = float('inf')
check = [False] * n
check_cnt = 0

for i in range(n):
    if target[i] < 1:
        check[i] = True
        check_cnt += 1

dfs(0, [0] * n, check_cnt)

print(answer)