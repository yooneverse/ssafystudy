'''
N명의 사람 둥글게
K번째 사람을 반복하여 제거

사람들이 제거되는 순서를 요세푸스 순열이라고 함
'''
'''
해당 인덱스 사람 제거하고
다음 사람을 찾으러 감

포인트
한 사람을 제거하게 되면 총 리스트의 길이가 바뀌면서
idx가 가리키는 사람이 다음 사람이 됨.
따라서 다음 사람은 idx + K 가 아니라 idx + K-1 이 됨
'''
N, K = map(int, input().split())

# 총 인원
people = [i for i in range(1, N+1)]

# 제거할 사람 인덱스
idx = 0

ans = []

# 로직 시작
while people:
    
    # 제거할 사람 인덱스
    # 인덱스가 people의 길이를 넘어가지 않도록
    idx = (idx + (K-1)) % len(people)
    
    # 해당 사람 제거
    # 출력 형식 준수 위해 숫자를 문자열로 바꿔줌 (''.join()는 문자열만 됨)
    ans.append(str(people.pop(idx)))

print('<' + ', '.join(ans) + '>')

