var express    = require('express')
var bodyParser = require('body-parser')
var fs = require('fs')
var app = express();

// parse application/json
app.use(bodyParser.json());

app.use('/mobile_signal/', function (req, res, next) {

    var a = req.body;
    console.log(a);
    res.send({status: 'OK'});
    console.log(a.mobile_signal[0])
});
app.listen(3001);
