function solution(x) {
    var n = x;
    var total = 0;
    while (n > 0) {
        total += n % 10;
        n = parseInt(n / 10);
    }
    
    return !(x % total)
}