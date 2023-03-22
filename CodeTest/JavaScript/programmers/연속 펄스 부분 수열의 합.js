// 1차 풀이
function solution(sequence) {
  const acc = [[0], [0]];

  let mul = 1;
  for (let i = 0; i < sequence.length; i++) {
    acc[0].push(acc[0][i] + sequence[i] * mul);
    acc[1].push(acc[1][i] + sequence[i] * mul * -1);
    mul *= -1;
  }

  let answer = -1e10;
  let minNum = [0, 0];
  for (let i = 1; i < sequence.length + 1; i++) {
    if (acc[0][i] > minNum[0]) {
      answer = Math.max(answer, acc[0][i] - minNum[0]);
    } else {
      minNum[0] = acc[0][i];
    }

    if (acc[1][i] >= minNum[1]) {
      answer = Math.max(answer, acc[1][i] - minNum[1]);
    } else {
      minNum[1] = acc[1][i];
    }
  }

  return answer;
}

// 2차 풀이
function solution(sequence) {
  let answer = -1e10;
  const accs = [0, 0];
  const minNums = [0, 0];

  let mul = 1;
  for (const num of sequence) {
    accs[0] += num * mul;
    accs[1] += num * mul * -1;

    for (let i = 0; i < 2; i++) {
      if (accs[i] < minNums[i]) minNums[i] = accs[i];
      else answer = Math.max(answer, accs[i] - minNums[i]);
    }

    mul *= -1;
  }

  return answer;
}
