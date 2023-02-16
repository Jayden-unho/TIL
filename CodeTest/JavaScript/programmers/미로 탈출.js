const dr = [-1, 0, 1, 0];
const dc = [0, 1, 0, -1];

function solution(maps) {
  const [R, C] = [maps.length, maps[0].length];
  let visited = Array(R)
    .fill(0)
    .map(() => Array(C).fill([500, -1]));
  let start, end;

  // 시작, 종료 좌표 찾기
  function findCoors() {
    maps.forEach((_, i) => {
      Array.from(maps[i]).forEach((v, j) => {
        if (v === "S") start = [i, j];
        else if (v === "E") end = [i, j];
      });
    });
  }

  // BFS 탐색
  function BFS(y, x) {
    let queue = [[y, x]];
    visited[y][x] = [0, 0];

    while (queue.length) {
      const next_queue = [];

      queue.forEach(([y, x]) => {
        [0, 1, 2, 3].forEach((d) => {
          const r = y + dr[d];
          const c = x + dc[d];

          // 좌표 벗어나거나 벽인 경우, 이동 불가
          if (0 > r || r >= R || 0 > c || c >= C || maps[r][c] === "X") return;
          if (
            (visited[y][x][1] === visited[r][c][1] &&
              visited[r][c][0] > visited[y][x][0] + 1) ||
            visited[y][x][1] > visited[r][c][1]
          ) {
            next_queue.push([r, c]);
            visited[r][c] = [visited[y][x][0] + 1, visited[y][x][1]];
            if (maps[r][c] === "L") visited[r][c][1]++;
          }
        });
      });

      queue = next_queue;
    }
    return visited[end[0]][end[1]][1] === 1 ? visited[end[0]][end[1]][0] : -1;
  }

  findCoors();
  const answer = BFS(...start);

  return answer;
}

console.log(solution(["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]));
console.log(solution(["LOOXS", "OOOOX", "OOOOO", "OOOOO", "EOOOO"]));
