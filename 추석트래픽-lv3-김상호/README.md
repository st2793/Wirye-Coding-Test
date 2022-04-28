# 추석 트래픽
### 풀이
```python
def solution(lines):
    answer = 0
    timeline = []
		# 시,분,초,밀리초를 모두 초로 통합, 밀리초는 소수점으로 유지
		# 시작시간,종료시간 2가지값을 timeline에 기존 순서대로저장
    for i in range(len(lines)):
        date,end,term = lines[i].split(' ')
        term = float(term[:-1])
        hour,minute,second = map(float,end.split(':'))
        end_total_sec = hour*3600 + minute*60 + second
        start_total_sec = end_total_sec - term
        timeline.append([start_total_sec,end_total_sec])
        
    #print(timeline)
    proc_nums = []
    for i in range(len(timeline)):
        proc_num = 1
        for j in range(i+1,len(timeline)):
            #print(timeline[i][1],timeline[j][0])
            prior_time_end = timeline[i][1]
            next_time_begin = timeline[j][0]
						# 전후작업 시간차, 1000밀리초 까지만 고려하기위해 round
            interval = round(next_time_begin-prior_time_end,3) 
            # 이전작업 종료시간, 이후작업 시작시간 비교
						# 또는 1000ms 오차가 있는 모든 경우는 처리개수 증가
            if (prior_time_end>=next_time_begin or interval<=0.998): #<=0.998 또는 <0.999
                #print(prior_time_end,next_time_begin,interval)
                proc_num+=1
        #print(proc_num)
        proc_nums.append(proc_num)
    answer = max(proc_nums)
    #print(answer)
    return answer
```
    
### 접근법
- 날짜는 제외시키고 끝난시간 시분초를 초로 통합한다
- 밀리초는 소수점으로 유지 (부동소수점문제가 생겨서 정수로 사용하는게 더 좋아보임)
- 처리시간으로 시작시간을 만든다
- 시작시간,끝난시간 배열을 만든다
- i번째와 i+1~n번째를 비교하며 최대값을 찾는다

### 의문
- 3,4번 테스트케이스의 차이?
    - 1000밀리초 까지 보기 때문에 0.001초 차이에 의해서 달라진다
- 1초범위내는 포함시킨다고 했는데 1.000초 그대로 쓰면 안돼나?
    - 4.002-5.000=0.998는 돼고 4.001-5.000=0.999는 안돼는거 보니 부동소수점문제인가?
    - 소수점을 사용하지 말고 밀리초까지 정수로 변경해서 사용하자
- 시작시간으로 정렬하고 비교한 사람도 있던데 차이는?
- datetime 사용의 어려움
    - time,datetime,date,timedelta등의 타입이 익숙치않아 포기