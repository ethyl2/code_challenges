/*
https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-javascript/use-recursion-to-create-a-countdown

Given a int n, return an array containing the ints n through 1. Use recursion.
If n=5, return [5,4,3,2,1]
*/

function countdown(n) {
  if (n < 1) {
    return [];
  }
  let countArray = countdown(n - 1);
  countArray.unshift(n);

  return countArray;
}

console.log(countdown(5));

const countdownEl = document.getElementById('countdown');

countdownEl.textContent += ' ' + countdown(5);

/*
Similar thing, but countup instead
*/
function countup(n) {
  if (n < 1) {
    return [];
  }
  const countArray = countup(n - 1);
  countArray.push(n);
  return countArray;
}

console.log(countup(5));

const countupEl = document.getElementById('countup');

countupEl.textContent += ' ' + countup(5);
