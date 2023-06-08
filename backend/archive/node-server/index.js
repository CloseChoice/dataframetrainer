const express = require('express');
const http = require('http');
const cors = require('cors')
const fs = require('fs');

const PORT = 3001

const app = express()
app.use(cors())

// const httpsServer = https.createServer(httpsOptions, app);
// 
// app.use((req, res, next) => {
//     if(req.protocol === 'http') {
//       res.redirect(301, `https://${req.headers.host}${req.url}`);
//     }
//     next();
// });
http.createServer(function (req, res) {
    res.writeHead(200, {'Content-Type': 'text/plain', 'Access-Control-Allow-Origin': '*'});
    res.write('Hello World!');
    res.end();
  }).listen(8080);

// app.get('/hashes/:hashes', (request, response) => {
//     return response.json("Dummy");
// })
// 
// httpsServer.listen(PORT, "0.0.0.0");