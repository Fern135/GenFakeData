const DataGenerator = require('../lib/DataGenerator');

const maxRequests = 14000;

const getUsers = (req, res) => {
    const count = parseInt(req.query.count) || parseInt(req.params.count) || 10;
    if(count > maxRequests) {
        res.status(400).send({ server : 'Too many users requested' });
    }
    const users = DataGenerator.generateUsers(count);
    res.json(users);
};

const getProducts = (req, res) => {
    const count = parseInt(req.query.count) || parseInt(req.params.count) || 10;
    if(count > maxRequests) {
        res.status(400).send({ server : 'Too many products requested' });
    }
    const products = DataGenerator.generateProducts(count);
    res.json(products);
};

const getCompanies = (req, res) => {
    const count = parseInt(req.query.count) || parseInt(req.params.count) || 10;
    if(count > maxRequests) {
        res.status(400).send({ server : 'Too many companies requested' });
    }
    const companies = DataGenerator.generateCompanies(count);
    res.json(companies);
};

const getCreditCards = (req, res) => {
    const count = parseInt(req.query.count) || parseInt(req.params.count) || 10;
    if(count > maxRequests) {
        res.status(400).send({ server : 'Too many credit cards requested' });
    }
    const creditCards = DataGenerator.generateCreditCards(count);
    res.json(creditCards);
};

const getJobs = (req, res) => {
    const count = parseInt(req.query.count) || parseInt(req.params.count) || 10;
    if(count > maxRequests) {
        res.status(400).send({ server : 'Too many jobs requested' });
    }
    const jobs = DataGenerator.generateJobs(count);
    res.json(jobs);
};

const getTextContents = (req, res) => {
    const count = parseInt(req.query.count) || parseInt(req.params.count) || 10;
    if(count > maxRequests) {
        res.status(400).send({ server : 'Too many text-contents requested' });
    }
    const contents = DataGenerator.generateTextContents(count);
    res.json(contents);
};

module.exports = {
    getUsers,
    getProducts,
    getCompanies,
    getCreditCards,
    getJobs,
    getTextContents,
};
