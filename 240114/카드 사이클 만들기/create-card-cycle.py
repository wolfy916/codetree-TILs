'''
카드 사이클 만들기 - 코드트리 실버3
분류 : 정렬
'''
import sys

# [A] 입력함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [Main]
if __name__ == "__main__":
    # [1] 데이터 입력
    N = int(input())
    nums = [int(input()) for _ in range(N)]
    target = [int(input()) for _ in range(N)]

    # [2] 정렬 로직
    cnt, max_size = 0, -1
    for i in range(N):
        if nums[i] == target[i]: continue
        size = 1
        nxt = target.index(nums[i])
        while nxt != i:
            nums[i], nums[nxt] = nums[nxt], nums[i]
            nxt = target.index(nums[i])
            size += 1
        cnt += 1
        max_size = max(max_size, size)
    
    print(cnt, max_size)