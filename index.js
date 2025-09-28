const express = require('express');
const dataRoutes = require('./routes/dataRoutes');
const util = require("./lib/util");

const app = express();
const operatingSys = util.getOs();

app.use('/api', dataRoutes);

app.use((req, res, next) => {
    res.status(404).send('Not Found');
    next();
});

// logging every request
app.use((req, res, next) => {
    console.log(`${new Date().toISOString()}: Incoming Request: ${req.method} ${req.url}`);
    next();
});

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
