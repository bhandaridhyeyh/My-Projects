import React, { useState } from "react";

export default function App() {
  const [text, setText] = useState("");
  const [output, setOutput] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
  setLoading(true);
  setOutput("");

  try {
    const res = await fetch("http://localhost:5000/api/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text }),
    });

    const data = await res.json();
    setOutput(data.entities);
  } catch (error) {
    console.error("Prediction error:", error);
    setOutput("Error predicting entities.");
  } finally {
    setLoading(false);
  }
};

  return (
    <div className="container mt-5">
      <div className="p-4 border border-dark rounded bg-light shadow">
        <h1 className="text-center mb-4 display-5 fw-bold">
          Hindi NER System
        </h1>

        <div className="mb-3">
          <label htmlFor="nerInput" className="form-label fw-semibold">
            Input:
          </label>
          <textarea
            id="nerInput"
            rows="4"
            className="form-control border-dark"
            placeholder="Example: महात्मा गांधी भारत के राष्ट्रपिता हैं।"
            value={text}
            onChange={(e) => setText(e.target.value)}
          ></textarea>
        </div>

        <button
          onClick={handleSubmit}
          className="btn btn-warning fw-bold border border-dark w-100"
          disabled={loading}
        >
          {loading ? "Predicting..." : "Submit"}
        </button>

        <div className="mt-4 p-3 bg-white border border-dark rounded">
          <h5 className="fw-semibold">Output:</h5>
          {loading ? (
            <p className="text-muted">Loading prediction...</p>
          ) : (
            <p>{output || "यहाँ परिणाम दिखेगा..."}</p>
          )}
        </div>
      </div>
    </div>
  );
}