var fruits = ["Apple", " Orange", " Pomegranate", " Guava", " Water Lemon"];
var grades = [];
var average;
var count = 0;

function displayFruits() {
  document.getElementById("fruits").innerHTML = fruits;
}

function addFruits() {
  var name = prompt("Type your fav fruit: ");
  fruits[fruits.length] = " " + name;
  document.getElementById("fruits").innerHTML = fruits;
}

function displayNum() {
  document.getElementById("numbers-1").innerHTML = grades;
}

function addNum() {
  grades[grades.length] = parseInt(prompt("Enter numbers"));
  document.getElementById("numbers-1").innerHTML = grades;
}

function findAverage() {
  if (grades.length > 0) {
    var num = 0;
    for (let index = 0; index < grades.length; index++) {
      num = num + grades[index];
    }
    average = num / grades.length;
    document.getElementById("ave").innerHTML = "The average is " + average;
  }
}

function clearArray() {
  grades.splice(0, grades.length);
}
