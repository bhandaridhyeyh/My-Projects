// Backend/controllers/nerController.js
const { spawn } = require("child_process");

exports.predictNER = (req, res) => {
  const inputText = req.body.text;
  const python = spawn("python", ["D:/22000810/Artificial Intelligence/AI_Hackathon/Backend/models/predict_wrapper.py", inputText]);

  let result = "";
  python.stdout.on("data", (data) => {
    result += data.toString();
  });

  python.stderr.on("data", (data) => {
    console.error("Python error:", data.toString());
  });

  python.on("close", (code) => {
    res.json({ entities: result.trim() });
  });
};
