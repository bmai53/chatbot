# BennyBot

A chatbot built and trained using a feed forward neural net, implemented in PyTorch. Detects user intent based on input, and provides a response.

[Click here to visit!](https://chat-with-bennybot.herokuapp.com/)

<img height=500px src="https://i.imgur.com/7GLdY8r.png" />

<img src="https://i.imgur.com/FuuJow1.png" />

## Try out the API! 

`GET https://chat-with-bennybot.herokuapp.com/chat`

#### Accepts: 

`Content-Type: application/json`

#### Request:

```
{
  "sentence": "hi how are you"
}
```

#### Response: 

```
{
  "msg": "Hi there, nice to meet you!",
  "tag": "greeting"
}
```

## Development

Deployed on Heroku using a Flask backend. 

UI developed using HTML/CSS/Bootstrap

