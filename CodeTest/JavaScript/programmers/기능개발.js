function solution(progresses, speeds) {
  let answer = []
  let taskIdx = 0
  
  let progress = progresses.map((v, i) => {
      return [v, i]
  })

  let tmp = 0
  while (progress.length > 0) {
      task = progress.shift()
      
      if (taskIdx === task[1] && task[0] >= 100) {
          cnt = 1 
          while (progress.length > 0) {
              nextTask = progress.shift()
              
              if (nextTask[0] < 100) {
                  progress.unshift(nextTask)
                  taskIdx = nextTask[1]
                  break
              }
              cnt++
          }
          answer.push(cnt) 
      } else {
          task[0] += speeds[task[1]]
          progress.push([task[0], task[1]])
      }
  }
  
  return answer
}

console.log(solution([93, 30, 55], [1, 30, 5]))
console.log(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))