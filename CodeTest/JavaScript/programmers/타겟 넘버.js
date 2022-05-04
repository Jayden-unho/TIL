function solution(numbers, target) {
  let answer = 0                      // 정답 변수
  
  function dfs(n, ans) {              // dfs 탐색 함수
    if (n >= numbers.length) {        // numbers 길이만큼 탐색 했다면
      if (ans === target) {           // 현재까지 정답이 타겟 숫자와 동일하면
          answer++                    // 정답 증가
      }
      return
    }    
      
    dfs(n + 1, ans + numbers[n])      // 현재 숫자를 더하기
    dfs(n + 1, ans - numbers[n])      // 현재 숫자를 빼기
  }
  
  dfs(0, 0)                           // dfs 탐색
      
  return answer;
}

console.log(solution([1, 1, 1, 1, 1], 3))
console.log(solution([4, 1, 2, 1], 4))