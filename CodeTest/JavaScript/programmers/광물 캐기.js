// 피로도 테이블
const fatigueTable = [
  [1, 1, 1],
  [5, 1, 1],
  [25, 5, 1],
];

// 각 광물의 인덱스
const mineralIdxs = { diamond: 0, iron: 1, stone: 2 };

function solution(picks, minerals) {
  let answer = 1e10;

  // 재귀 함수
  function sol(minerals, fatigue) {
    // 현재까지 구한 최소값보다 크거나 같으면 더 이상 탐색하지 않음
    if (answer <= ans) return;
    // 곡괭이를 다 썼거나 모든 광석을 다 캤으면 최소값 업데이트
    else if (picks.every((p) => p === 0) || minerals.length === 0)
      return (answer = ans);

    // 3가지 곡괭이에 대해 반복문 실행
    for (let i = 0; i < 3; i++) {
      // 해당 곡괭이가 남아있지 않으면 통과
      if (picks[i] === 0) continue;

      // 곡괭이 사용
      picks[i]--;
      // 현재 곡괭이로 5개의 광물을 캐고 쌓이는 피로도 계산
      const additional = minerals
        .slice(0, 5)
        .reduce((p, c) => p + fatigueTable[i][mineralIdxs[c]], 0);
      // 다음 탐색을 위한 재귀 호출
      sol(minerals.slice(5), fatigue + additional);
      // 다른 경우 탐색을 위해 곡괭이 반납
      picks[i]++;
    }
  }

  sol(minerals, 0);

  return answer;
}
