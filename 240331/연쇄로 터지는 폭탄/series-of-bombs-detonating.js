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
        answer = Math.max(answer, bfs(arr[i]));
        for (let i=0; i<n; i++) {
            bombs.set(arr[i], false);
        };
    };

    return answer;

    function bfs(start) {
        let cnt = 0;
        let queue = [[start, 1]];
        bombs.set(start, true);
        while (queue.length > 0) {
            let [v, dis] = queue.shift();
            cnt += 1;
            for (let i=v-dis; i<=v+dis; i++) {
                if (bombs.get(i) === false) {
                    queue.push([i, dis + 1]);
                    bombs.set(i, true);
                }
            }
        }
        return cnt;
    }
};

const input = require('fs').readFileSync("/dev/stdin").toString().split('\n');
console.log(solution(input));