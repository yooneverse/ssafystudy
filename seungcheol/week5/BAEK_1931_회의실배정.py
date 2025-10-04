# 회의 수 입력
N = int(input())

# 회의의 정보 저장
# dictionary: key=회의 시작시간 ,value=끝나는 시간
dictionary = {}

for _ in range(N):
    # 회의 시작시간, 끝나는 시간
    s, e = map(int, input().split())

    # 회의시작 시간이 key로 없으면 추가
    if dictionary.get(s) is None:
        dictionary[s] = [e]
    # 회의 끝나는 시간이 더 있으면 추가
    else:
        dictionary[s].append(e)

# 회의 시작시간 모음 및 정렬
start = list(dictionary.keys())
start.sort()

# 가장 많은 회의 수
cnt = 0

# 회의 끝나는 시간
out = 0

# 회의 수 확인
for i in range(len(start)):
    tmp = dictionary[start[i]]
    tmp.sort()

    for end in tmp:
        # 회의 종료 후 새 회의 시작
        if out <= start[i]:
            if start[i] == end:
                cnt += 1
                continue
            else:
                cnt += 1
                out = end
                break
        # 더 빨리 끝나는 회의가 있는 경우
        elif end < out:
            out = end

print(cnt)