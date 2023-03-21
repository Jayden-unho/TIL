function solution(m, n, startX, startY, balls) {
  function isValid(x, y, nx, ny) {
    if (startX === nx) {
      return Math.min(startY, ny) <= y && y <= Math.max(startY, ny);
    } else if (startY === ny) {
      return Math.min(startX, nx) <= x && x <= Math.max(startX, nx);
    }
    return false;
  }

  const calcDist = (nx, ny) => (startX - nx) ** 2 + (startY - ny) ** 2;

  const answer = balls.map(([x, y]) => {
    const ans = [
      [x, -y],
      [-x, y],
      [x, 2 * n - y],
      [2 * m - x, y],
    ].map(([nx, ny]) => {
      return isValid(x, y, nx, ny) ? 1e10 : calcDist(nx, ny);
    });
    return Math.min(...ans);
  });

  return answer;
}
