const express = require('express');
const router = express.Router();
const dataController = require('../controllers/dataController');

// Define routes for each type of data
router.get('/users/:count?', dataController.getUsers); // √√
router.get('/products/:count?', dataController.getProducts); // √√
router.get('/companies/:count?', dataController.getCompanies); // √√
router.get('/credit-cards/:count?', dataController.getCreditCards);// √√
router.get('/jobs/:count?', dataController.getJobs); // √√
router.get('/text-contents/:count?', dataController.getTextContents); // √√

module.exports = router;
