/*
  From https://leetcode.com/problems/zigzag-conversion/

  The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
  P   A   H   N
  A P L S I I G
  Y   I   R

  And then read line by line: "PAHNAPLSIIGYIR"
*/

/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function(s, numRows) {
    if (numRows === 1) {
      return s
    }
    const initialCharArray = s.split('')
    let resultingArrays = []
    for (let i=0; i<numRows; i++) {
      let innerArray = []
      resultingArrays.push(innerArray)
      }

    let direction = 'up'
    index = 0
    for (let i=0; i<initialCharArray.length; i++) {
      if (index === 0) {
        direction = 'down'
        resultingArrays[index].push(initialCharArray[i])
        index++
      } else if (index === numRows - 1) {
        direction = 'up'
        resultingArrays[index].push(initialCharArray[i])
        index--
      } else if (direction === 'down') {
        resultingArrays[index].push(initialCharArray[i])
        index++
      } else {
        resultingArrays[index].push(initialCharArray[i])
        index--
      }
    }

    let resultingString = ''
    for (let i=0; i<resultingArrays.length; i++) {
      let arrayString = resultingArrays[i].join('')
      resultingString += arrayString
    }

    return resultingString
}

// console.log('answer: ' + convert("AB", 1))
// console.log('answer: ' + convert("PAYPALISHIRING", 3))

const stringForm = document.getElementById('form-string')
const stringInput = document.getElementById('input-string')
const rowCountInput = document.getElementById('input-row-count')
const answerInput = document.getElementById('answer')

stringForm.addEventListener('submit', (e) => {
  e.preventDefault()
  answerInput.textContent = convert(stringInput.value, rowCountInput.value)
})
