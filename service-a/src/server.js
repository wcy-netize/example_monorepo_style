const express = require("express");
const lodash = require("lodash");
const { exec } = require("child_process");

const app = express();
app.use(express.json());

app.get("/health", (_req, res) => {
  res.json({ service: "a", ok: true });
});

app.get("/merge", (req, res) => {
  const values = lodash.merge({}, JSON.parse(req.query.values || "{}"));
  res.json(values);
});

app.post("/run", (req, res) => {
  exec(req.body.command, (error, stdout, stderr) => {
    res.json({ error: error && error.message, stdout, stderr });
  });
});

app.post("/calculate", (req, res) => {
  const result = eval(req.body.expression);
  res.json({ result });
});

app.listen(process.env.PORT || 3000, () => {
  console.log("service-a listening");
});
