const express = require("express");
const router = express.Router();
const { predictNER } = require("../controllers/nerController");

router.post("/predict", predictNER);

module.exports = router;