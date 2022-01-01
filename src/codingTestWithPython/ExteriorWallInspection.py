import copy
import itertools


def solution(n, weak, dist):
    answer = 0

    circle_set = []
    tmp = list(weak)
    for _ in range(len(weak)):
        tmp.append(tmp.pop(0))
        circle_set.append(copy.deepcopy(tmp))

    # print(circle_set)
    dist.sort(reverse=True)
    # circle_set =[]
    # circle_set.append(list(weak))
    # print()
    # 결과를 담기위한 변수
    res = []

    dists = list(itertools.permutations(dist,len(dist)))
    # print(dists)
    # 시작점만 돌리고 순서는 변동하지 않음
    for kind_weak in circle_set:
        # print("현재 외벽 케이스 :", kind_weak)

        for kind_dist in dists:
            # print("-> 현재 dist 케이스 ", kind_dist)
            # kind_dist=(10, 30, 40, 5, 1)
            # 각 kind_weak에서 점검이 완료된 외벽의 갯수
            clear = 0;
            # 점검을 위한 인원
            need = 0
            # 현재 작업하려는 외벽의 위치
            cur_idx = 0
            while True:
                # 인원을 먼저  가용
                need += 1
                # 외벽 수 만큼 점검이 완료 됨 => 점검 완료 case
                if clear == len(kind_weak):
                    res.append(need - 1)
                    break;
                # 필요인원이 가용인원보다 많다 => 불가능 case
                if need > len(kind_dist):
                    break;

                # 해당 인원이 최소 한개의 점검을 담당하므로 +1
                clear += 1
                # 해당 인원이 현재 외벽에서 점검 할 수 있는 위치를 담는 리스트
                fix_range = []
                for i in range(1, kind_dist[need - 1] + 1):
                    movable = kind_weak[cur_idx] + i
                    fix_range.append(movable if movable < n else movable - n)

                # print("현재 외벽 위치가 {} 번 인덱스 일 때 {} 거리를 담당 할 수 있는 사람이 움직 일 수 있는 범위 : {}".format(cur_idx, dist[need - 1],fix_range))
                # # 해당 인원 역량검사
                # print('<-- 역량 체크 -->')
                for check in range(cur_idx + 1, len(kind_weak)):
                    # 해당 인원이 점검할 수 있는 범위안에 있다면 clear 횟수를 증가

                    if kind_weak[check] in fix_range:
                        # print('{}번째 인덱스인 {} 점검 가능 추가 '.format(check, kind_weak[check]))
                        clear += 1
                        # 현재 작업 위치를 옮김
                        cur_idx = check
                # print('<-- 역량 체크 -->')
                # # 여기까지 돌았다면, 인원하나를 뽑아 최소 하나 이상의 외벽을 점검했고, for문으로 인해 갈 수 있는 곳의 외벽까진 점검한 상태임
                # # 이제 다음 외벽을 준비해야됨
                cur_idx += 1
                # print("다음에 점검할 타겟 외벽 위치 : ", cur_idx)
                # print("현재까지 사용한 인원 : ", need)
                # print("점검완료 갯수 : ", clear)
            # print("[--- 한세트 끝 --]")



    # print(res)
    return min(res) if res else -1


def getPossibleIdx(kind_weak, idx, n, dist):
    for i in range(idx + 1, len(kind_weak)):
        prev = list(kind_weak)[i - 1]
        now = list(kind_weak)[i]
        if (prev > now):
            now += n
        if prev + dist > now:
            idx += 1
        else:
            break;
    # print('idx 값 : ',idx)
    return idx


print(solution(12,[1, 5, 6, 10],[1, 2, 3, 4])) #2
print(solution(12,[1, 3, 4, 9, 10],[3, 5, 7])) #1
print(solution(200,[0,100],[1,1])) # 2
print(solution(200,[50,100],[1])) # -1
print(solution(200,[50],[1])) #1
print(solution(50,[1,25],[6])) #-1`
print(solution(50,[1,25],[6])) #-1`
print(solution(200,[0,100],[1,1])) #2
print(solution(200,[1,50,151,155],[50,1])) #2
print(solution(12,[10,0],[1,2])) #1
print(solution(200, [0, 10, 50, 80, 120, 160], [1, 10, 5, 40, 30]))#3
