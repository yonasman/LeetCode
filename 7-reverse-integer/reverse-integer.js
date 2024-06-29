/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    // handling the sign of number
   let sign = x < 0 ? -1 : 1;
   x = Math.abs(x);
    // variable to store reversed number
    let reversedNum = 0;
    let digit = 0;
    while(x != 0) {
        digit = x % 10;
        reversedNum = reversedNum * 10 + digit;
        x = Math.floor(x / 10); 
    }
    
    reversedNum *= sign;
    
    if(reversedNum < (-2) ** 31 || reversedNum > (2**31 - 1)) {
        return 0;
    }
    
   return reversedNum; 
   
}; 