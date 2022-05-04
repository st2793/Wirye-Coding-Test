def solution(lines):
    answer = 0
    start_time = []
    end_time = []

    for t in lines:
        time = t.split(" ")
        start_time.append(get_start_time(time[1], time[2]))
        end_time.append(get_time(time[1]))
    for i in range(len(lines)):
        cnt = 0
        cur_end_time = end_time[i]
        
        # i번째는 현재 자신의 시작 시간, i 이하는 그 이전의 시작 시간이므로 no count
        for j in range(i, len(lines)):
            # 처리 시간은 시작&끝 시간 모두를 포함하기에 -999가 아닌 -1000을 함
            if cur_end_time > start_time[j] - 1000:
                # 구간 내 겹치면 cnt + 1
                cnt += 1
        answer = max(answer, cnt)
    return answer

# time을 정수 type으로 변환
def get_time(time):
    hour = int(time[:2]) * 3600
    minute = int(time[3:5]) * 60
    second = int(time[6:8])
    millisecond = int(time[9:])
    return (hour + minute + second) * 1000 + millisecond

# 시간 시간 구하기
def get_start_time(time, duration_time):
    # [:-1] 맨 뒤의 item 1개 빼고 전부 => 문자열 's'를 제외한 처리 시간(sec)
    n_time = duration_time[:-1]
    # millisecond 가 포함된 수식과의 합산을 위해 1000 를 곱셈
    int_duration_time = int(float(n_time) * 1000)
    # 1을 더한 최종값
    return get_time(time) - int_duration_time + 1


"""
[해설]
(1) 입력 받은 문자열을 split와 slice notation ':' 로 자르고, 

(2) Hour, Minute, Second 부분으로 각 부분을 second를 기준으로 합쳐서 계산하였습니다.
    => (hour * 3600) + (minute * 6) + second
    => 계산한 time 값에 1000을 곱하여, Millisecond에 다시 맞췄습니다.

(3) 각 처리 시간을 cur_end_time & start_time 배열로 나누고 이중 for문에 넣습니다.
    => start_time 배열은 cur_end_time 배열보다 앞서므로 -1 초(1000ms)를 한 뒤, 
        두 배열 값을 비교하여 cur_end_time 값이 더 크면 같은 시간대로 간주하여 cnt + 1을 하며 한 바퀴를 돕니다.
    => 그리드 알고리즘에 따라 특정 구간이 아닌 겹치는 가장 큰 값(cnt)을 찾으며, 
        겹치는 구간이 없을 경우인 answer = 0 을 넣고 max를 통해 정답을 도출합니다.
        => 만약 겹치는 구간이 반드시 1개 이상 존재한다면 max를 쓸 필요는 없습니다.
"""


"""
[Way to solve]
(1) 완전 탐색
(2) 다이나믹 프로그래밍
(3) 그리디 알고리즘 
    => task schedulling problem
"""


"""
[해설]
https://velog.io/@mrbartrns/%ED%8C%8C%EC%9D%B4%EC%8D%AC-1%EC%B0%A8%EC%B6%94%EC%84%9D-%ED%8A%B8%EB%9E%98%ED%94%BD-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%A0%88%EB%B2%A83

[참고 자료 : greedy algorithm]
https://hanamon.kr/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%ED%83%90%EC%9A%95%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-greedy-algorithm/?ckattempt=1

[참고 자료 : slice notation ':']
https://hashcode.co.kr/questions/74/%ED%8C%8C%EC%9D%B4%EC%8D%AC-slice-notation-%EC%93%B0%EB%8A%94%EA%B1%B0%EC%A2%80-%EC%95%8C%EB%A0%A4%EC%A3%BC%EC%84%B8%EC%9A%94
"""
