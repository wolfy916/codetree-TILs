_ = int(input())
nums = list(map(int, input().split()))
print(*sorted(nums, reverse=True))