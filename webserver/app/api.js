const express = require('express');
const { Client } = require('pg');
const app = express();
const cors = require('cors');
app.use(cors({
    "origin": "*",
    "methods": "GET,HEAD,PUT,PATCH,POST,DELETE",
    "preflightContinue": false,
    "optionsSuccessStatus": 204
}));

// Crea una nuova istanza del client PostgreSQL
const client = new Client({
    user: 'admin',
    host: 'db',
    database: 'body-performance',
    password: 'admin',
    port: 5432,
});

app.use(express.json());

app.post('/query', async (req, res) => {
  const { age, gender, height, weight, body_fat, diastolic, systolic, bend_forward, grip_force, sit_ups, broad_jump, classValue } = req.body;
  const query = 'INSERT INTO body_performance(age, gender, height, weight, body_fat, diastolic, systolic, bend_forward, grip_force, sit_ups, broad_jump, class) VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12)';

  try {
    await client.query(query, [age, gender, height, weight, body_fat, diastolic, systolic, bend_forward, grip_force, sit_ups, broad_jump, classValue]);
    res.status(201).send('Performance data added successfully');
  } catch (error) {
    console.error(error);
    res.status(500).send('Error inserting performance data');
  }
});

// Avvia il server API sulla porta 3001
app.listen(3001, () => {
  console.log('API server listening on port 3001');
});



