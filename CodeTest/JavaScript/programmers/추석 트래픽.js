function solution(lines) {
  let answer = 0          // 정답
  const timeline = {}     // 타임라인을 저장할 객체
  
  lines.map(v => v.split(' ')).forEach(v => {
      const hour = parseInt(v[1].slice(0, 2)) * 3600000       // 시간을 밀리초로 변경
      const minute = parseInt(v[1].slice(3, 5)) * 60000       // 분을 밀리초로 변경
      const second = parseFloat(v[1].slice(6)) * 1000         // 초를 밀리초로 변경
      
      let end = hour + minute + second                                            // 종료 시간
      const duration = parseFloat(v[2].replace('s', '')) * 1000                   // 소요 시간
      const start = end - duration + 1                                            // 시작 시간
      end += 1000                                                                 // 1초 동안의 처리량을 구해야하므로 종료 시간에 1초를 추가
      
      timeline[start] = timeline[start] === undefined ? 1 : timeline[start] + 1   // 시작 시간을 키값으로 값은 1
      timeline[end] = timeline[end] === undefined ? -1 : timeline[end] - 1        // 종료 시간을 키값으로 값은 -1
  })
  
  let cnt = 0
  Object.keys(timeline).sort((a,b) => a - b).forEach(v => {                       // 타임라인에 있는 시간들을 오름차순으로 정렬하여 1초동안 처리 가능한 최대 개수 구하기
      cnt += timeline[v] 
      answer = Math.max(answer, cnt)
  })
  
  return answer
}