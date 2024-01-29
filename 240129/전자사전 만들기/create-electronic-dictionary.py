'''
전자사전 만들기 - 코드트리 골드4
분류 : 전처리
'''
import sys

# [A] 입력함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [Main]
if __name__ == "__main__":
    # [1] 데이터 입력
    N, T = map(int, input().split())
    words = [input() for _ in range(N)]
    orders = [tuple(input().split()) for _ in range(T)]

    # [2] 데이터 초기화
    idx = {words[i]: i + 1 for i in range(N)}
    ref = dict()

    # [3] 사전 기록
    words.sort()
    for word in words:
        for i in range(1, len(word) + 1):
            if ref.get(word[:i]):
                ref[word[:i]].append(idx[word])
            else:
                ref[word[:i]] = [idx[word]]

    # [4] 결과 출력
    for n, word in orders:
        n = int(n)
        if not ref.get(word) or len(ref[word]) < n:
            print(-1)
        else:
            print(ref[word][n - 1])