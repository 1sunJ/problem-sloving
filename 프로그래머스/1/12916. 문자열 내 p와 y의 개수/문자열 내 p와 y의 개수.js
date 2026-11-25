function solution(s){
    var answer = true;
    s = s.toLowerCase();

    var pp = 0;
    var yy = 0;
    for (const c of s) {
        if (c === 'p')
            pp++;
        if (c === 'y')
            yy++;
    }

    return pp == yy;
}