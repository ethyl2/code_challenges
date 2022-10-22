/* From https://leetcode.com/problems/climbing-stairs
  You are climbing a staircase. It takes n steps to reach the top.
  Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

  Example 1:

  Input: n = 2
  Output: 2
  Explanation: There are two ways to climb to the top.
  1. 1 step + 1 step
  2. 2 steps

  Example 2:

  Input: n = 3
  Output: 3
  Explanation: There are three ways to climb to the top.
  1. 1 step + 1 step + 1 step
  2. 1 step + 2 steps
  3. 2 steps + 1 step
*/

var climbStairs = function(n) {
  return fib(n) // non-recursive way
  // return innerClimbStairs(n, 1) // recursive way
}

let cache = {}

function innerClimbStairs(n, acc) {
  let waysCount = acc
  if (n > 1) {
    let accString = acc.toString()
    let firstKey = (n-1).toString() + ',' + accString
    let firstValue = cache[firstKey] ?? innerClimbStairs(n-1, acc)
    let secondKey = (n-2).toString() + ',' + accString
    let secondValue = cache[secondKey] ?? innerClimbStairs(n-2, acc)
    waysCount = firstValue + secondValue
  }
  return waysCount
}

function fib(num) {
  let x = 1
  let y = 0
  let temp

  while(num >=0) {
    temp = x
    x = x + y
    y = temp
    num--
  }

  return y
}

const result = climbStairs(5) // 8
// console.log(result)

const stairsEl = document.getElementById('stairs')

function createStaircase(stairsCount) {
  let paddingBottom = 0
  for (let i=0; i < stairsCount; i++) {
    const stairEl = document.createElement('div')
    stairEl.textContent = '|^^'
    stairEl.style.marginBottom = paddingBottom + 'px'
    stairsEl.append(stairEl)
    paddingBottom += 30
  }
}

createStaircase(8)

const stairsForm = document.getElementById('stairs-form')
const stairsInput = document.getElementById('stairs-input')
const answerEl = document.getElementById('answer')

stairsForm.addEventListener('submit', (e) => {
  e.preventDefault()
  removeAllChildNodes(stairsEl)
  createStaircase(stairsInput.value)
  answerEl.textContent = climbStairs(stairsInput.value)
})

function removeAllChildNodes(parent) {
    while (parent.firstChild) {
        parent.removeChild(parent.firstChild);
    }
}
