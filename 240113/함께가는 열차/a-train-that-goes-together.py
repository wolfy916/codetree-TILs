'''
함께가는 열차 - 코드트리 실버5
분류 : 그리디
'''
import sys

# [A] 입력함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [Main]
if __name__ == "__main__":
    # [1] 데이터 입력 및 초기화
    N = int(input())
    info = [tuple(map(int, input().split())) for _ in range(N)]
    
    answer = 1
    v = info[N - 1][1]
    for i in range(N - 2, -1, -1):
        if info[i][1] > v: continue
        v = info[i][1]
        answer += 1

    print(answer)