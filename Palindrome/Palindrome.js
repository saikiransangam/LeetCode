var isPalindrome = function(x) {
  const isNegative = x < 0 ? true : false;
  
  if(isNegative){
      return false;
  }
  const temp = x;
  let reverse = 0;
  
  while(x>0){
      reverse = (reverse * 10) + (x % 10);
      x = parseInt(x/10);
  }
  return reverse == temp;
};