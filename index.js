const express = require('express');
const dataRoutes = require('./routes/dataRoutes');
const util = require("./lib/util");

const app = express();
const operatingSys = util.getOs();

app.use((req, res, next) => {
    res.status(404).send('Not Found');
});

// logging every request
app.use((req, res, next) => {
    console.log(`Incoming Request: ${req.method} = ${req.url}\t${req.statusCode}`);
    next();
});


app.use('/api', dataRoutes);


const PORT = 3000;

app.listen(PORT, () => {
    switch(operatingSys) { 
        case 'win32':
            console.log(`Server running on => localhost:${PORT}`);
            break;

        case 'darwin':
        case 'linux':
            console.log(`Server running on => 127.0.0.1:${PORT}`);
            break;

        default:
            console.log("Unkown OS");
            break;
    }
});
