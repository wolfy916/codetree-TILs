const solution = (input) => {
    let [a, b] = input[0].split(' ').map((v) => +v);
    let answer = 0;
    let cur = a;
    let dis = 1;
    let nxt;
    while (true) {
        nxt = a + dis;
        if (cur <= b && b <= nxt) {
            answer += Math.abs(b - cur);
            break;
        } else if (nxt <= b && b <= cur) {
            answer += Math.abs(b - cur);
            break;
        } else {
            answer += Math.abs(nxt - cur);
            cur = nxt;
            dis *= -2;
        }
    }

    return answer;
}

const input = require('fs').readFileSync("/dev/stdin").toString().split('\n');
console.log(solution(input));