import sys

def input():
    return sys.stdin.readline().rstrip('\n')

if __name__ == "__main__":
    n = int(input())
    coords = [tuple(map(int, input().split())) for _ in range(n)]
    stack = []
    answer = 0

    for x, y in coords:
        if len(stack) < 1:
            answer += 1

        while stack:
            if stack[-1] < y:
                answer += 1
                break
            else:
                stack.pop()

        if y > 0:
            stack.append(y)
    
    if len(stack) > 0:
        answer += 1

    print(answer)