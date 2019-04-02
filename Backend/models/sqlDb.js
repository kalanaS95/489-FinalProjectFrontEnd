var mysql = require('mysql');

//Set up the connection
const connection = mysql.createConnection({
    host: 'localhost',
    database: 'iStats',
    user: 'root',
    password: 'Huskyyoungwoo1'
});

//Make connection
connection.connect(function(err) {
    if (err) {
        console.error('Error connecting: ' + err.stack);
    } else {
        console.log("Connected to SQL DB!");
    }
}); 

//Export connection for use in Model code
module.exports = connection; //export