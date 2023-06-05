var req = new XMLHttpRequest();
req.open('GET', 'http://127.0.0.1:5000/challenges/1', false);
req.send(null);
let k = req.responseText;
console.log(k);


let t;
fetch('http://127.0.0.1:5000/challenges/1')
  .then((response) => {t = response.json()})
  .then((data) => console.log(data)).then((data) => data);

let t = fetch('http://127.0.0.1:5000/challenges/1')
  .then((response) => {return response.json()})

console.log("This is t ", t);
console.log(t);