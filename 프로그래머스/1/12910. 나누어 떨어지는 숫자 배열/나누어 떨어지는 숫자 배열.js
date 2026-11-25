function solution(arr, divisor) {
    var answer = [];
    for (const x of arr) {
        if (x % divisor === 0) {
            answer.push(x)
        }
    }
    
    answer.sort((a, b) => a - b)
    if (answer.length == 0) {
        answer.push(-1)
    }
    
    return answer;
}