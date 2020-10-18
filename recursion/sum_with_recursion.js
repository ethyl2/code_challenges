/*
https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-javascript/replace-loops-using-recursion

Write a recursive function, sum(arr, n), that returns the sum of the first n elements of an array arr.
*/

function sum(arr, n) {
  if (n <= 0) {
    return 0;
  }
  return sum(arr, n - 1) + arr[n - 1];
}

const sumEl = document.getElementById('sum');
const result = sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 5);
sumEl.textContent += result;

/*
Same, but with multiply
*/

function multiply(arr, n) {
  if (n <= 0) {
    return 1;
  } else {
    return multiply(arr, n - 1) * arr[n - 1];
  }
}

const multiplyEl = document.getElementById('multiply');
const result2 = multiply([1, 2, 3, 4, 5, 6, 7, 8, 9], 5);
multiplyEl.textContent += ' ' + result2;
