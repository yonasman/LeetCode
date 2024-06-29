/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
  if(x < 0) {
        return false;
    }
    let originalNum = x;
    let reversedNum = 0;
    while(originalNum != 0) {
        let digit = originalNum % 10;
        reversedNum = reversedNum * 10 + digit;
        originalNum = Math.floor(originalNum / 10); 
    }
    
   return x === reversedNum;  
};