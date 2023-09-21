function findDigit(num, nth) {
    if (nth <= 0) {
        return -1;
    }
    
    const numStr = Math.abs(num).toString();
    
    if (nth <= numStr.length) {
        return parseInt(numStr[numStr.length - nth]);
    } else {
        return 0;
    }
}

console.log(findDigit(4569, 2));     // Output: 2
console.log(findDigit(-2825, 3));   // Output: 8
console.log(findDigit(0, 20));      // Output: 0
console.log(findDigit(68, 0));      // Output: -1
