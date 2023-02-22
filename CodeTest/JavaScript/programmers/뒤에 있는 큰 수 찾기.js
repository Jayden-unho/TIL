function solution(numbers) {
  const answer = [];
  const stack = [];

  for (let i = 1; i < numbers.length; i++) {
    const prev = numbers[i - 1];
    const curr = numbers[i];

    if (prev < curr) {
      answer.push(curr);
      while (stack.length > 0) {
        const idx = stack.pop();
        const num = numbers[idx];

        if (num < curr) {
          answer[idx] = curr;
        } else {
          stack.push(idx);
          break;
        }
      }
    } else {
      answer.push(-1);
      stack.push(i - 1);
    }
  }
  answer.push(-1);

  return answer;
}
