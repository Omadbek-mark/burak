// TASK N
function palindromCheck(palindrom: string) {
  let checkPal = palindrom.split("").reverse().join("");

  if (palindrom !== checkPal) {
    return false
  }
  else {
    return true
  }
}

const result = palindromCheck("radar");
console.log("TASK N:", result);
const result1 = palindromCheck("typeScript");
console.log("TASK N-2:", result1);


// // TASK M
// function getSquareNumbers(arr: number[]) {
//   let result = [];

//   for (let numb of arr) {
//     let getSquare = { number: numb, square: numb * numb };
//     result.push(getSquare);
//   }

//   return result;
// }

// const result = getSquareNumbers([25, 15, 9]);
// console.log("TASK M:", result);


// // TASK L
// function reverseSentence(ele: string) {
//   let words = ele.split(" ");

//   let reversedWords = [];

//   for (let word of words) {
//     let ele1 = word.split("")
//     let getReverse = ele1.reverse();
//     let reversedSentence = getReverse.join("");
//     reversedWords.push(reversedSentence);
//   }

//   return reversedWords.join(" ");
// } 

// const result1 = reverseSentence("we are on typeScript now");
// console.log("TASK L:", result1);


// // TASK K
// function countVowels(word: string) {
//   let vowels = "aeiouAEIOU";
//   let founded_vowels = [];
//   let count = 0;

//   for (let letter of word) {
//     if (vowels.includes(letter)) {
//       count++;
//       founded_vowels.push(letter);
//     }
//   }

//   return {count, founded_vowels};
// }

// const result3 = countVowels("Never Give Up!")
// console.log("TASK K:", result3);