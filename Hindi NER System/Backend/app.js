const express = require("express");
const cors = require("cors");
const bodyParser = require("body-parser");

const app = express();
app.use(cors());
app.use(bodyParser.json());

const predictRoute = require("./routes/predict");
app.use("/api", predictRoute);

module.exports = app;