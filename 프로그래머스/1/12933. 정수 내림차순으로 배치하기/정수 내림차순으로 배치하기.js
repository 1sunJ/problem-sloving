function solution(n) {
    var answer = 0;
    var str = String(n)
    var arr = [...str]
    arr = arr.map((c) => parseInt(c))
    arr.sort()
    arr.reverse()
    
    str = arr.join('')
    return parseInt(str)
}