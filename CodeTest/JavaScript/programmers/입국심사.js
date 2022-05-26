function solution(n, times) {
  let answer = 0                                        // 정답 변수
  let min_time = 1                                      // 심사를 모두 마치는 최소 시간
  let max_time = n * Math.max(...times)                 // 심사를 모두 마치는 최대 시간
  
  while (min_time <= max_time) {                        // 이분 탐색
    const mid = parseInt((min_time + max_time) / 2)     // 최소와 최대의 중간 값
    
    let people = 0                                      // 현재 시간에서 심사 가능한 인원
    times.forEach(t => people += parseInt(mid / t))     // 심사관별로 해당 시간에 심사 가능한 인원 누적
    
    if (people >= n) {      // n명 이상 심사 가능하면
      answer = mid          // 현재 시간 기록
      max_time = mid - 1    // 더 적은 시간으로 심사 가능한지 탐색
    } else {                // 모두 심사 불가능하면
      min_time = mid + 1    // 더 많은 시간으로 심사 가능한지 탐색
    }
  }

  return answer
}