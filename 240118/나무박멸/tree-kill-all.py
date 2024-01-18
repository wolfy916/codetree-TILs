'''
나무박멸 - 코드트리 골드4
분류 : 구현, 시뮬레이션
'''
import sys

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] 나무 성장 및 번식
def growing_tree():
    breeding = []
    for i in range(N):
        for j in range(N):
            # 벽과 제초제 제외
            if area[i][j] < 1 or medicine[i][j] > 0: continue
            empty_space_cnt = 0  # 인접한 빈 공간 카운트
            tree_cnt = 0         # 인접 나무 수 카운트
            coords = []          # 인접 좌표 저장
            for di, dj in cross:
                ni, nj = i + di, j + dj
                if ni < 0 or nj < 0 or ni >= N or nj >= N: continue
                if medicine[ni][nj] > 0: continue
                # 인접 빈 공간의 경우
                if area[ni][nj] == 0:
                    empty_space_cnt += 1
                    coords.append((ni, nj))
                # 인접 나무의 경우
                elif area[ni][nj] > 0:
                    tree_cnt += 1
            area[i][j] += tree_cnt  # 나무 성장
            if empty_space_cnt < 1: continue
            for ci, cj in coords:
                breeding.append((ci, cj, area[i][j] // empty_space_cnt))  # 나무 번식 데이터
    # 나무 번식
    for ni, nj, b in breeding:
        area[ni][nj] += b

# [C] 제초제 유지 기간 감소
def reduce_medicine():
    for i in range(N):
        for j in range(N):
            if medicine[i][j] < 1: continue
            medicine[i][j] -= 1

# [D] 가장 많이 나무를 박멸할 수 있는 제초제 살포 좌표 탐색
def search_medicine_point():
    maxV = pi = pj = 0
    for i in range(N):
        for j in range(N):
            # 벽과 제초제 제외
            if area[i][j] < 1 or medicine[i][j] > 0: continue
            # 제초제 살포시 박멸할 수 있는 나무 수 카운트
            remove_tree_cnt = area[i][j]
            for di, dj in diagonal:
                ni, nj = i, j
                for _ in range(K):
                    ni += di; nj += dj;
                    if ni < 0 or ni >= N or nj < 0 or nj >= N: break
                    if area[ni][nj] <= 0: break
                    remove_tree_cnt += area[ni][nj]
            # 제초제 살포 좌표 갱신
            if maxV < remove_tree_cnt:
                maxV = remove_tree_cnt
                pi = i; pj = j;
    return pi, pj, maxV

# [E] 제초제 살포
def spray_medicine(pi, pj):
    area[pi][pj] = 0
    medicine[pi][pj] = C
    for di, dj in diagonal:
        ni, nj = pi, pj
        for _ in range(K):
            ni += di; nj += dj;
            if ni < 0 or ni >= N or nj < 0 or nj >= N: break
            medicine[ni][nj] = C
            if area[ni][nj] < 1: break
            area[ni][nj] = 0

# [main]
if __name__ == '__main__':
    # [1] 데이터 입력 및 초기화
    N, M, K, C = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(N)]
    medicine = [[0] * N for _ in range(N)]           # 제초제 유지 기간 기록
    cross = [(-1, 0), (1, 0), (0, -1), (0, 1)]       # + 방향
    diagonal = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # x 방향
    answer = 0

    # [2] 시뮬레이션 M번 반복
    for _ in range(M):
        # 나무 성장과 번식
        growing_tree()
        # 제초제 유지 기간 감소
        reduce_medicine()
        # 제초제 살포할 좌표 탐색 및 살포시 박멸하는 나무수 카운트
        pi, pj, remove_tree_cnt = search_medicine_point()
        answer += remove_tree_cnt
        # 제초제 살포
        spray_medicine(pi, pj)
    
    print(answer)