const dr = [-1, 0, 1, 0];
const dc = [0, 1, 0, -1];

function solution(maps) {
  const answer = [];
  const R = maps.length;
  const C = maps[1].length;
  const visited = Array(R)
    .fill(0)
    .map(() => Array(C).fill(false));

  function DFS(y, x) {
    let result = 0;
    const stack = [[y, x]];

    while (stack.length > 0) {
      const [y, x] = [...stack.pop()];
      if (visited[y][x]) continue;

      visited[y][x] = true;
      result += parseInt(maps[y][x]);
      for (let k = 0; k < 4; k++) {
        const [r, c] = [y + dr[k], x + dc[k]];

        if (0 > r || r >= R || 0 > c || c >= C) continue;
        if (visited[r][c] || maps[r][c] === "X") continue;
        stack.push([r, c]);
      }
    }

    return result;
  }

  maps.forEach((v, i) => {
    Array.from(maps[i]).forEach((v, j) => {
      if (v === "X" || visited[i][j]) return;

      const num = DFS(i, j);
      answer.push(num);
    });
  });

  if (answer.length === 0) return [-1];
  return answer.sort((a, b) => a - b);
}

console.log(solution(["X591X", "X1X5X", "X231X", "1XXX1"]));
console.log(solution(["XXX", "XXX", "XXX"]));
