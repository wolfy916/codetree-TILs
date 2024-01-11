'''
루프 탈출 - 코드트리 실버 2
분류 : 구현, 시뮬레이션
'''
import sys
from collections import deque as dq

# [A] 입력함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [Main]
if __name__ == "__main__":
    # [1] 데이터 입력
    n = int(input())
    nums = [0] + [int(input()) for _ in range(n)]

    # [2] 인접 리스트 생성
    adjL = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        adjL[nums[i]].append(i)

    # [3] bfs
    answer = 0
    visited = [False] * (n + 1)
    q = dq([0])
    while q:
        v = q.popleft()
        for w in adjL[v]:
            if visited[w]: continue
            visited[w] = True
            answer += 1
            q.append(w)
    
    print(answer)