var num1 = parseInt(window.prompt("Enter number 1 : "));
var num2 = parseInt(window.prompt("Enter number 2 : "));
let opera = input();
var result;

function input() {
  var oper = window.prompt(
    "Enter the operation you want to perform : (+, -, *, /, %)"
  );
  return oper;
}
function add(num1, num2) {
  result = num1 + num2;
  return result;
}
function subtract(num1, num2) {
  result = num1 - num2;
  return result;
}
function multiply(num1, num2) {
  result = num1 * num2;
  return result;
}
function divide(num1, num2) {
  result = num1 / num2;
  return result;
}
function modulus(num1, num2) {
  result = num1 % num2;
  return result;
}

if (opera == "+") {
  add(num1, num2);
  console.log("The answer is : " + result);
} else if (opera == "-") {
  subtract(num1, num2);
  console.log("The answer is : " + result);
} else if (opera == "*") {
  multiply(num1, num2);
  console.log("The answer is : " + result);
} else if (opera == "/") {
  divide(num1, num2);
  console.log("The answer is : " + result);
} else if (opera == "%") {
  modulus(num1, num2);
  console.log("The answer is : " + result);
} else {
  window.alert("Invalid Input..");
  input();
}
