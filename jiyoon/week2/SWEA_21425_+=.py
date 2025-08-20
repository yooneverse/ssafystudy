T = int(input()) #테스트케이스 불러오기
 
for tc in range(1, T+1): #각 케이스 순회
    A, B, N = map(int, input().split()) #정수형 변수 띄어쓰기 있는 값
    # x = A
    # y = B
     
    count = 0 # 연산횟수 초기화
     
    #직접 A,B 사용
    while N >= A and N >= B:  #A , B 값이 N보다 작거나 같을 때
         
        if A < B:
            A += B
        else:
            B += A
        count += 1
     
    print(count)
        