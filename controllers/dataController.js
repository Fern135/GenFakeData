const DataGenerator = require('../lib/DataGenerator');

const getUsers = (req, res) => {
    const count = parseInt(req.query.count) || parseInt(req.params.count) || 10;
    const users = DataGenerator.generateUsers(count);
    res.json(users);
};

const getProducts = (req, res) => {
    const count = parseInt(req.query.count) || parseInt(req.params.count) || 10;
    const products = DataGenerator.generateProducts(count);
    res.json(products);
};

const getCompanies = (req, res) => {
    const count = parseInt(req.query.count) || parseInt(req.params.count) || 10;
    const companies = DataGenerator.generateCompanies(count);
    res.json(companies);
};

const getCreditCards = (req, res) => {
    const count = parseInt(req.query.count) || parseInt(req.params.count) || 10;
    const creditCards = DataGenerator.generateCreditCards(count);
    res.json(creditCards);
};

const getJobs = (req, res) => {
    const count = parseInt(req.query.count) || parseInt(req.params.count) || 10;
    const jobs = DataGenerator.generateJobs(count);
    res.json(jobs);
};

const getTextContents = (req, res) => {
    const count = parseInt(req.query.count) || parseInt(req.params.count) || 10;
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
