let dictionary;
const http_call = () => {
    let req = new XMLHttpRequest();
    req.open('GET', 'http://127.0.0.1:5000/challenges/1/', false);
    req.send(null);
    let k = JSON.parse(req.responseText);
    console.log(`This is k ${k}`);
    console.log(`This is k ${k.response}`);
    let field = document.getElementById("field");
    let stringified = k.response;
    field.innerHTML = JSON.stringify(stringified);
    console.log(`wrote in field value`);
    let eingabe = document.getElementById("Eingabe");
    eingabe.value = stringified;
    dictionary = stringified;
    return dictionary
};

// const http_call = () => {
// fetch('http://127.0.0.1:5000/challenges/1')
//   .then((response) => response.json())
//   .then((data) => console.log(data)).then((data) => data).catch((data) => console.log(data));
// 
// fetch('https://verkehr.autobahn.de/o/autobahn/A1/services/roadworks')
//   .then((response) => response.json())
//   .then((data) => console.log(data)).then((data) => data).catch((data) => console.log(data));
// }

let los  = document.getElementById('los');
los.addEventListener ('click', http_call, true);
