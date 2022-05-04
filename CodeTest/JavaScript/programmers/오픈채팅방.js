function solution(record) {
  let answer = [];                                    // 정답 리스트
  let logs = [];                                      // 들어가거나 나간 로그 기록들
  let user = {};                                      // 유저 아이디 정보, 유저아이디: 이름
  
  record.forEach(v => { 
      let splited = v.split(' ');                     // 띄어쓰기로 구분
      
      if (splited[0] === 'Enter') {                   // 들어온 경우, 유저 아이디와 이름을 기록하고 로그도 기록
          user[splited[1]] = splited[2]               
          logs.push([splited[1], '님이 들어왔습니다.'])
      } else if (splited[0] === 'Leave') {            // 나간 경우, 나간 기록 로그에 기록
          logs.push([splited[1], '님이 나갔습니다.'])
      } else {                                        // 이름 변경한 경우, 객체에서 이름 변경
          user[splited[1]] = splited[2]
      }
  })
  
  answer = logs.map(v => {        // 로그를 반복
      v[0] = user[v[0]]           // 유저 아이디를 이름으로 변경
      return v.join('')           // 문자열로 합쳐서 반환
  })
  
  return answer;
}