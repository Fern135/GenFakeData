const express = require('express');
const router = express.Router();
const dataController = require('../controllers/dataController');

const routesHelp = {
    "users"         : "localhost:3000/api/users/:count?",
    "products"      : "localhost:3000/api/products/:count?",
    "companies"     : "localhost:3000/api/companies/:count?",
    "credit-cards"  : "localhost:3000/api/credit-cards/:count?",
    "jobs"          : "localhost:3000/api/jobs/:count?",
    "text-contents" : "localhost:3000/api/text-contents/:count?",
}

router.get('/help', (req, res) => res.send(routesHelp));

// Define routes for each type of data
router.get('/users/:count?',         dataController.getUsers); // √√
router.get('/products/:count?',      dataController.getProducts); // √√
router.get('/companies/:count?',     dataController.getCompanies); // √√
router.get('/credit-cards/:count?',  dataController.getCreditCards);// √√
router.get('/jobs/:count?',          dataController.getJobs); // √√
router.get('/text-contents/:count?', dataController.getTextContents); // √√

module.exports = router;

