/*
Given 2 ints, return array of ints that start with 1st int and end with 2nd int.
Use recursion.

https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-javascript/use-recursion-to-create-a-range-of-numbers
*/

function rangeOfNumbers(startNum, endNum) {
  if (startNum === endNum + 1) {
    return [];
  }
  const countArray = rangeOfNumbers(startNum + 1, endNum);
  countArray.unshift(startNum);
  return countArray;
}

const rangeEl = document.getElementById('range');
const numbers = rangeOfNumbers(1, 5);

rangeEl.textContent += ' ' + numbers;
