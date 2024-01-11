'''
루프 탈출 - 코드트리 실버 2
분류 : 유니온 파인드
'''
import sys

# [A] 입력함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [Main]
if __name__ == "__main__":
    # [1] 데이터 입력
    n = int(input())
    nums = [0] + [int(input()) for _ in range(n)]

    # [2] 루프 체크 및 탐색
    is_loop = [False] * (n + 1)
    for i in range(1, n + 1):
        if is_loop[i] or nums[i] < 1: continue
        visited = [i]
        while not is_loop[nums[i]] and nums[i] not in visited:
            if nums[i] == 0: break
            visited.append(nums[i])
            i = nums[i]
        else:
            for j in visited:
                is_loop[j] = True

    # [3] 출력
    print(is_loop.count(False) - 1)