import sys

def input():
    return sys.stdin.readline().rstrip('\n')

if __name__ == "__main__":
    n = int(input())
    coords = [tuple(map(int, input().split())) for _ in range(n)]

    stack = []
    answer = 0
    for x, y in coords:
        while stack:
            if stack[-1] < y:
                answer += 1
                break
            else:
                stack.pop()
        stack.append(y)

    print(answer)