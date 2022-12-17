const fs = require("fs");

const input = fs.readFileSync("./input.txt").toString().split("\n");
// const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const T = parseInt(input[0]);

for (let i = 1; i < T + 1; i++) {
  const num = parseInt(input[i * 3 - 2]);
  const prev = input[i * 3 - 1];
  const after = input[i * 3];

  let white = 0;
  let black = 0;

  for (let j = 0; j < num; j++) {
    if (prev[j] === after[j]) continue;
    if (after[j] === "B") black++;
    if (after[j] === "W") white++;
  }

  const answer = Math.min(white, black) + Math.abs(white - black);
  console.log(answer);
}
