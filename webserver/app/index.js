const express = require('express');
const serveStatic = require('serve-static');
const pg = require('pg');
const app = express();
const cors = require('cors');
app.use(cors({
    "origin": "*",
    "methods": "GET,HEAD,PUT,PATCH,POST,DELETE",
    "preflightContinue": false,
    "optionsSuccessStatus": 204
}));

app.use(serveStatic('public')); // 'public' è la cartella contenente i file statici

app.listen(8080, () => {
    console.log('Server avviato sulla porta 8080');
});


module.exports = pg.Client;