function solution(k, tangerine) {
  let answer = 0;
  let remain = k;

  const cnts = {};
  tangerine.forEach((v) => (cnts[v] = (cnts[v] ?? 0) + 1));
  const sortedCnts = Object.keys(cnts).sort((a, b) => cnts[b] - cnts[a]);

  for (key of sortedCnts) {
    if (remain <= 0) break;

    remain -= cnts[key];
    answer++;
  }

  return answer;
}
