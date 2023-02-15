function solution(x, y, n) {
  const dp = {};
  dp[x] = 0;

  let nums = [x];
  while (nums.length && !dp[y]) {
    const nextNums = [];
    nums.forEach((num) => {
      [n + num, num * 2, num * 3].forEach((v) => {
        if (!dp[v] && v <= y) {
          nextNums.push(v);
          dp[v] = dp[num] + 1;
        }
      });
    });
    nums = [...nextNums];
  }

  return dp[y] === undefined ? -1 : dp[y];
}
