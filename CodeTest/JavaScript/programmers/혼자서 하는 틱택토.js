const winConditionCoors = [
  [
    [0, 0],
    [0, 1],
    [0, 2],
  ], // 1행
  [
    [1, 0],
    [1, 1],
    [1, 2],
  ], // 2행
  [
    [2, 0],
    [2, 1],
    [2, 2],
  ], // 3행
  [
    [0, 0],
    [1, 0],
    [2, 0],
  ], // 1열
  [
    [0, 1],
    [1, 1],
    [2, 1],
  ], // 2열
  [
    [0, 2],
    [1, 2],
    [2, 2],
  ], // 3열
  [
    [0, 0],
    [1, 1],
    [2, 2],
  ], // 왼쪽 대각선
  [
    [0, 2],
    [1, 1],
    [2, 0],
  ], // 오른쪽 대각선
];

function solution(board) {
  function chkWinner() {
    const winner = new Set();

    for (let i = 0; i < winConditionCoors.length; i++) {
      let s = 0;
      for ([r, c] of winConditionCoors[i]) {
        if (board[r][c] === "O") s++;
        else if (board[r][c] === "X") s--;
      }
      if (s === 3) winner.add(1); // 'O'
      else if (s === -3) winner.add(2); // 'X'
    }

    if (winner.size > 1) return -1;
    else if (winner.size === 1) return winner.values().next().value;
    return 0;
  }

  function chkCount() {
    let [circle, cross] = [0, 0];

    board.forEach((row) => {
      Array.from(row).forEach((v) => {
        if (v === "O") circle++;
        else if (v === "X") cross++;
      });
    });

    return [circle, cross];
  }

  const winner = chkWinner();
  const [circle, cross] = chkCount();

  if (winner === -1) return 0;
  else if (winner === 0 && (circle === cross || circle - 1 === cross)) return 1;
  else if (winner === 1 && circle - 1 === cross) return 1;
  else if (winner === 2 && circle === cross) return 1;
  return 0;
}
