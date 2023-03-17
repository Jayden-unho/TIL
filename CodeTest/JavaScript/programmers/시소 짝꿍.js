const multiple = [1, 3 / 2, 4 / 2, 2 / 3, 4 / 3, 2 / 4, 3 / 4];

function solution(weights) {
  let answer = 0;
  let cnts = {};

  weights.forEach((w) => {
    multiple.forEach((m) => (answer += cnts[m * w] ?? 0));
    cnts[w] = (cnts[w] ?? 0) + 1;
  });

  return answer;
}
