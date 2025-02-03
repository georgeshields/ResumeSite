//DO NOT USE THIS FILE FOR RUNNING GPT

const express = require('express');
// require OpenAI from 'openai';
const { Configuration, OpenAIApi } = require('openai');
const cors = require('cors');
const bodyParser = require('body-parser');
require('dotenv').config();

const app = express();
app.use(cors());
app.use(bodyParser.json());

if (!process.env.OPENAI_API_KEY) {
  throw new Error('OPENAI_API_KEY is not set');
}

const openai = new OpenAI({
    apiKey: process.env['OPENAI_API_KEY'],
});

app.post('/chat', async (req, res) => {
  try {
    const userMessage = req.body.message;

    const response = await openai.createChatCompletion({
      model: 'gpt-3.5-turbo',
      messages: [
        {
          role: 'system',
          content: 'You are a helpful version of George. Answer questions about his experience, skills, etc.',
        },
        { role: 'user', content: userMessage },
      ],
    });

    const assistantReply = response.data.choices[0].message.content;
    res.json({ reply: assistantReply });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});