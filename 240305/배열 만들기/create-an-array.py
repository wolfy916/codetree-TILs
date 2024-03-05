def dfs(cnt, cur):
    if sum(cur) < 1:
        return cnt

    for i in range(n):
        if cur[i] % 2:
            cur[i] -= 1
            cnt += 1

    if sum(cur) < 1:
        return cnt

    return dfs(cnt + 1, list(map(lambda x: x // 2, cur)))

n = int(input())
target = list(map(int, input().split()))
print(dfs(0, target))