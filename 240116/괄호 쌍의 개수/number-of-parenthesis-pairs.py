'''
괄호 쌍의 개수 - 코드트리 골드3
분류 : LR technic
'''
import sys
from collections import Counter

# [A] 입력함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [Main]
if __name__ == "__main__":
    A = input()

    N = len(A)
    counter = Counter(A)

    if abs(counter['('] - counter[')']) != 2:
        print(0)
        exit()

    L = [[0, 0] for _ in range(N)]
    R = [[0, 0] for _ in range(N)]
    link = {'(': 0, ')': 1}
    left, right = [0, 0], [0, 0]
    for i in range(N):
        left[link[A[i]]] += 1
        right[link[A[N - i - 1]]] += 1
        L[i][0] = left[0]
        L[i][1] = left[1]
        R[N - i - 1][0] = right[0]
        R[N - i - 1][1] = right[1]
    
    L = [[0, 0]] + L
    R = R + [[0, 0]]

    answer = 0
    tmp = '(' if counter['('] > counter[')'] else ')'
    for i in range(1, N + 1):
        # print(L[i - 1], A[i - 1], R[i])
        if A[i - 1] != tmp: continue
        if L[i - 1][0] >= L[i - 1][1]:
            answer += 1
            
    print(answer)