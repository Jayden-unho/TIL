function solution(n, computers) {
  let answer = 0                                  // 정답 변수
  let visited = Array(n).fill(0)                  // 각 노드의 방문 여부를 저장
  let linked = Array(n).fill(0).map(() => [])     // 각 노드별 연결 관계 (2차원 배열)
  
  function dfs(start) {                 // DFS 탐색
    let stack = Array(1).fill(start)    // 초기 스택
    
    while (stack.length > 0) {          // 스택에 값이 남아있으면 반복
      let node = stack.pop()
      if (!visited[node]) {             // 해당 노드를 방문하지 않았으면, 방문 처리
        visited[node] = 1
        linked[node].forEach(v => {     // 연결된 노드들 추가
          stack.push(v)
        })
      }
    }
  }

  for (let i=0; i<n; i++) {             // 연결 관계 정리
    for (let j=i+1; j<n; j++) {
      if (computers[i][j] === 1) {
        linked[i].push(j)
        linked[j].push(i)
      }
    }
  }

  for (i=0; i<n; i++) {     // 노드들 반복하여
    if (!visited[i]) {      // 네트워크에 속하지 않은 노드이면
      dfs(i)
      answer++              // 네트워크 개수 추가
    }
  }


  return answer
}

console.log(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
console.log(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))