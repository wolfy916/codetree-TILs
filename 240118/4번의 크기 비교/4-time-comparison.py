a = int(input())
nums = list(map(int, input().split()))
for i in range(4):
    print(1 if a > nums[i] else 0)