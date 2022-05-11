function solution(numbers) {
  var answer = 0
  let number = numbers.split('')
  let selected = Array(number.length).fill(0)
  let combs = new Set()
  
  function cases(n, ans) {
    if (n >= number.length) {
      console.log(ans)
      ans ? combs.add(parseInt(ans)) : null
      return
    }
    
    for (let i=0; i<=number.length; i++) {
      if (!selected[i]) {
        selected[i] = 1
        cases(n+1, ans + number[i])
        selected[i] = 0
        cases(n+1, ans)
      }
    }
  }
  
  cases(0, '')

  console.log(combs)
  
  let primeNumbers = Array(Math.max(...combs)).fill(true)

  console.log(primeNumbers)


  return answer;
}

console.log(solution('17'))
console.log(solution('011'))