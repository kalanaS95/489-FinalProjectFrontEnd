'use strict';

//Import controller functions



module.exports = function(app) {
    var sgPlayer = require('../controllers/apiController');

    //Routes
    app.route('/')
    .post()
    .get();
    
};