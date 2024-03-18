import sys

def input():
    return sys.stdin.readline().rstrip('\n')

if __name__ == "__main__":
    n = int(input())
    coords = [tuple(map(int, input().split())) for _ in range(n)]
    ref = dict()
    answer = 0

    for x, y in coords:
        keys = ref.keys()
        if len(keys) > 0:
            for key in sorted(keys, reverse=True):
                if key > y:
                    del ref[key]
                    answer += 1
                else:
                    break
            if not ref.get(y) and y > 0:
                ref[y] = True
        else:
            ref[y] = True

    answer += len(ref.keys())

    print(answer)