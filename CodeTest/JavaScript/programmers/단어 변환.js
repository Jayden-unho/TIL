function solution(begin, target, words) {
  let answer = 1e10                         // 최솟값을 구해야하므로 초기에 가장 높은 값으로 초기화
  const N = words.length                    // 변환 가능한 단어의 개수
  const visited = Array(N).fill(false)      // 해당 단어로 변환을 했었는지 확인을 위함
  
  function sol(n, now, ans) {               // 남은 변환 가능 단어 개수, 현재 단어, 변경한 횟수
    if (now === target) {                   // 타겟과 단어가 같다면
      answer = Math.min(answer, ans)        // 현재까지 기록된 횟수와 비교하여 더 작은 값 저장
      return
    } else if (n === 0) {                   // 모든 단어를 탐색해봤다면 종료
      return
    }
    
    words.forEach((word, idx) => {
      let diff = Array.from(word).filter((v, idx) => v !== now[idx])    // 현재 단어와 변경 가능한 단어의 알파벳 비교하여 다른 갯수만큼 반환
      if (diff.length === 1 && !visited[idx]) {                         // 알파벳 다른 개수가 1개이고, 변환한적이 없다면
        visited[idx] = true                                             // 변환하여 다음 단어 탐색
        sol(n-1, word, ans+1)
        visited[idx] = false
      }
    })
  }
  
  sol(N, begin, 0)
  
  return answer === 1e10 ? 0 : answer       // 값이 변하지 않았다면, 가능한 경우가 없으므로 0 반환
}

console.log(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
console.log(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))