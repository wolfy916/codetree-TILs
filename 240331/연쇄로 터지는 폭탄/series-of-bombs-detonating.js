const solution = (input) => {
    let line = 0;
    const n = +input[line++];
    const arr = input.slice(1, ).map((v) => +v);

    const bombs = new Map();
    for (let i=0; i<n; i++) {
        bombs.set(arr[i], false);
    };

    let answer = 0;
    for (let i=0; i<n; i++) {
        answer = Math.max(answer, bfs(arr[i], 1));
        for (let i=0; i<n; i++) {
            bombs.set(arr[i], false);
        };
    };

    return answer;

    function bfs(start) {
        let cnt = 1;
        let queue = [[start, 1]];
        while (queue.length > 0) {
            let [v, dis] = queue.shift();
            if (bombs.get(v) === false) {
                bombs.set(v, true);
                cnt += 1;
                queue.push([v + dis, dis + 1]);
                queue.push([v - dis, dis + 1]);
            }
        }
        return cnt;
    }
};

const input = require('fs').readFileSync("/dev/stdin").toString().split('\n');
console.log(solution(input));