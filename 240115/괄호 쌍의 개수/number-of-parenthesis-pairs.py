'''
괄호 쌍의 개수 - 코드트리 골드3
분류 : 그리디?
'''
import sys

# [A] 입력함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [Main]
if __name__ == "__main__":
    A = input()

    N = len(A)
    cnt = {'(': 0, ')': 0}
    answer = 0
    for i in range(N):
        cnt[A[i]] += 1
        if cnt['('] + 1 < cnt[')']:
            answer += cnt[')'] - 1

    if abs(cnt['('] - cnt[')']) != 2:
        print(0)
        sys.exit()
    
    print(answer)