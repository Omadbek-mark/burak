// TASK M
function getSquareNumbers(arr: number[]) {
  let result = [];

  for (let numb of arr) {
    let getSquare = { number: numb, square: numb * numb };
    result.push(getSquare);
  }

  return result;
}

const result = getSquareNumbers([25, 15, 9]);
console.log(result);
