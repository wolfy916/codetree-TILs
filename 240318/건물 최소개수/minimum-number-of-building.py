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
                stack.append(y)
            elif stack[-1] > y:
                stack.pop()
                answer += 1
            else:
                break
        if len(stack) < 1 and y > 0:
            stack.append(y)

    answer += len(stack)

    print(answer)