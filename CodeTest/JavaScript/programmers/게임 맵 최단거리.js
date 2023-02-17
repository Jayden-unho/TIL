const dr = [-1, 0, 1, 0];
const dc = [0, 1, 0, -1];

function solution(maps) {
  const [R, C] = [maps.length, maps[0].length];
  const visited = Array(R)
    .fill(0)
    .map(() => Array(C).fill(-1));

  function BFS() {
    let queue = [[0, 0]];
    visited[0][0] = 1;

    while (queue.length) {
      const next_queue = [];
      queue.map(([y, x]) => {
        [0, 1, 2, 3].map((k) => {
          const [r, c] = [y + dr[k], x + dc[k]];

          if (
            0 > r ||
            r >= R ||
            0 > c ||
            c >= C ||
            visited[r][c] !== -1 ||
            maps[r][c] !== 1
          )
            return;
          visited[r][c] = visited[y][x] + 1;
          next_queue.push([r, c]);
        });
      });

      queue = next_queue;
    }
  }

  BFS();

  return visited[R - 1][C - 1] === -1 ? -1 : visited[R - 1][C - 1];
}

console.log(
  solution([
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 1],
  ])
);
console.log(
  solution([
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1],
  ])
);
