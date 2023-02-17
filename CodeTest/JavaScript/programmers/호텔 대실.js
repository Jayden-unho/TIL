function solution(book_time) {
  const day = 24 * 60;
  const rooms = Array(day + 11).fill(0);

  book_time.forEach((_, i) => {
    book_time[i].forEach((v, j) => {
      const minutes =
        parseInt(v.slice(0, 2)) * 60 + parseInt(v.slice(3, 5)) + 1;

      if (j === 0) rooms[minutes]++;
      else rooms[minutes + 10]--;
    });
  });

  for (let i = 1; i < rooms.length; i++) {
    rooms[i] = rooms[i] + rooms[i - 1];
  }

  return Math.max(...rooms);
}
