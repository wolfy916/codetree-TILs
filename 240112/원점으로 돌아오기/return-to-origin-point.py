'''
원점으로 돌아오기 - 코드트리 골드5
분류: 백트랙킹
'''
import sys

# [A] 입력함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] 백트랙킹 탐색 함수
def dfs(idx, cnt, dx, dy):
    global answer

    x, y = coords[idx]

    # 모든 점을 방문했을때
    if cnt >= N + 1:
        # 원점으로 이동 가능하면 카운트
        if x == 1000:
            dir = 1 if y <= 1000 else -1
            if dy * dir <= 0: answer += 1
        elif y == 1000:
            dir = 1 if x <= 1000 else -1
            if dx * dir <= 0: answer += 1
        return

    # 수직 이동
    for i in adjX[x]:
        if visited[i]: continue
        dir = 1 if y <= coords[i][1] else -1
        if dy * dir > 0: continue
        visited[i] = True
        dfs(i, cnt + 1, 0, dir)
        visited[i] = False

    # 수평 이동
    for i in adjY[y]:
        if visited[i]: continue
        dir = 1 if x <= coords[i][0] else -1
        if dx * dir > 0: continue
        visited[i] = True
        dfs(i, cnt + 1, dir, 0)
        visited[i] = False

# [Main]
if __name__ == "__main__":
    # [1] 데이터 입력 및 초기화
    N = int(input())
    coords = [(1000, 1000)]
    for _ in range(N):
        x, y = map(int, input().split())
        coords.append((x + 1000, y + 1000))
    
    # [2] -1000 ~ 1000 좌표 범위를 커버하기 위한 인접리스트 생성
    adjX = [[] for _ in range(2001)]
    adjY = [[] for _ in range(2001)]
    for i in range(N + 1):
        x, y = coords[i]
        adjX[x].append(i)
        adjY[y].append(i)

    # [3] 중복 탐색 방지 + dfs
    visited = [False] * (N + 1)
    visited[0] = True  # 원점 출발
    answer = 0
    dfs(0, 1, 0, 0)  # dfs(coords의 인덱스, 방문한 점의 갯수, x이동방향, y이동 방향)

    # [4] 출력
    print(answer)