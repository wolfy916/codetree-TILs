import sys
from collections import Counter

def input():
    return sys.stdin.readline().rstrip('\n')

if __name__ == "__main__":
    N, L = map(int, input().split())
    arr = list(map(int, input().split()))

    answer = 0
    counter = Counter(arr)
    keys = sorted(counter.keys(), reverse=True)
    for key in keys:
        if counter[key] >= key:
            answer = key
            break
        elif key - counter[key] <= counter[key - 1]:
            answer = key
            break

    print(answer)