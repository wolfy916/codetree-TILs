'''
전자사전 만들기 - 코드트리 골드4
분류 : 전처리
'''
import sys

# [A] 입력함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] 이분 탐색
def binary_search(word, is_lower=True):
    result = 0
    left, right = 0, N - 1
    while left <= right:
        mid = (left + right) // 2
        if words[mid].startswith(word):
            result = mid
            if is_lower:
                right = mid - 1
            else:
                left = mid + 1
        elif words[mid] < word:
            left = mid + 1
        elif words[mid] > word:
            right = mid - 1
    return result

# [Main]
if __name__ == "__main__":
    # [1] 데이터 입력
    N, T = map(int, input().split())
    words = [input() for _ in range(N)]
    orders = [tuple(input().split()) for _ in range(T)]

    # [2] 데이터 초기화
    idx = {words[i]: i + 1 for i in range(N)}
    words.sort()
    
    # [4] 결과 출력
    for n, word in orders:
        start = binary_search(word, True)
        end = binary_search(word, False)
        if end - start + 1 >= int(n):
            print(idx[words[start + int(n) - 1]])
        else:
            print(-1)