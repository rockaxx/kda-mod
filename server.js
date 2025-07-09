const express = require('express');
const path = require('path');
const cors = require('cors');

const app = express();
const PORT = 3000;

// ✅ Povoliť všetky CORS requesty
app.use(cors());

// ✅ Slúžiť celý spacemap priečinok ako public
app.use('/', express.static(path.join(__dirname, 'spacemap')));

// Logger voliteľný
app.use((req, res, next) => {
  console.log(`[REQ] ${req.method} ${req.url}`);
  next();
});

app.use((req, res) => {
  res.status(404).send('404 Not Found');
});

app.listen(PORT, () => {
  console.log(`🌍 Server beží na http://localhost:${PORT}/`);
});
