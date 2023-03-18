// 위, 오른쪽, 아래, 왼쪽
const dr = [-1, 0, 1, 0];
const dc = [0, 1, 0, -1];

function solution(board) {
  // 로봇의 시작 좌표 구하기
  function getStartCoors() {
    for (let i = 0; i < R; i++) {
      for (let j = 0; j < C; j++) {
        if (board[i][j] === "R") return [i, j];
      }
    }
  }

  // 주어진 좌표에서 특정 방향으로 이동
  function move(direction, y, x) {
    let [r, c] = [y, x];

    // 좌표가 범위 내에 있고 벽에 도착하지 않으면 계속 이동
    while (isValidCoors(r, c) && board[r][c] !== "D") {
      [r, c] = [r + dr[direction], c + dc[direction]];
    }

    // 범위 벗어나기 직전이거나 벽 바로 직전 좌표를 반환
    return [r - dr[direction], c - dc[direction]];
  }

  // BFS 탐색
  function BFS(y, x) {
    queue = [[y, x]];
    visited[y][x] = 0;

    while (queue.length > 0) {
      nQueue = [];
      for ([r, c] of queue) {
        // 목표 지점에 도착했다면 탐색 종료
        if (board[r][c] === "G") return visited[r][c];

        const currVisit = visited[r][c] + 1;
        for (let k = 0; k < 4; k++) {
          const [nr, nc] = move(k, r, c);
          // 아직 방문하지 않았으면 이동 확정
          if (visited[nr][nc] === -1) {
            visited[nr][nc] = currVisit;
            nQueue.push([nr, nc]);
          }
        }
      }
      queue = nQueue;
    }
    return -1;
  }

  const [R, C] = [board.length, board[0].length];
  const visited = Array(R)
    .fill(0)
    .map(() => Array(C).fill(-1));
  const isValidCoors = (y, x) => 0 <= y && y < R && 0 <= x && x < C;

  const [startY, startX] = getStartCoors();
  const answer = BFS(startY, startX);

  return answer;
}
