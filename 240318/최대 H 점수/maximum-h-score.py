import sys
from collections import Counter

def input():
    return sys.stdin.readline().rstrip('\n')

if __name__ == "__main__":
    N, L = map(int, input().split())
    arr = list(map(int, input().split()))

    maxV = max(arr)
    counter = [0] * (maxV + 1)
    for num in arr:
        counter[num] += 1

    for num in range(maxV, 0, -1):
        counter[num - 1] += counter[num]

    answer = 1
    for num in range(maxV, 0, -1):
        if num <= counter[num]:
            answer = num
            break
        elif num <= counter[num] + L <= counter[num - 1]:
            answer = num
            break

    print(answer)