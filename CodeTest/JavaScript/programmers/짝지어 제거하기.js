function solution(s) {
  let stack = []                                  // 문자열 하나하나 저장할 스택

  Array.from(s).forEach(v => {                    // 문자열을 배열로 변경하여 알파벳 하나씩 반복
    if (stack.length === 0) {                   // 스택이 비어있으면, 문자 추가
      stack.push(v)
    } else if (stack[stack.length - 1] === v) {   // 스택의 가장 최근 값이 현재 문자랑 동일하면, 짝지어서 제거 가능
      stack.pop()
    } else {                                    // 스택의 가장 최근 값이랑 현재 값이랑 다르면, 스택에 현재 값 추가
      stack.push(v)
    }
  })

  return stack.length === 0 ? 1 : 0       // 스택이 비어 있으면, 모두 제거되었으므로 1 반환, 그렇지 않으면 0 반환
}