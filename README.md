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

## Running the App

Clone or download the repo, then do either of the following:

Run `python3 cli_chat.py` to test the chatbot in the terminal.

Run `flask run` to start the web app and server. Open `http://127.0.0.1:5000/` to see the app!

## Training

Include a custom `intents.json` file in the following format:

```
{
  "intents": [
    {
     "tag": "bot",
      "patterns": [
        "Are you real",
        "Are you a bot",
        "Who are you?"
      ]
    },

    ...

  ]
}

```

Also include a `responses.json` file in the following format:

```
{
  "response_data": [
  {
      "tag": "bot",
      "responses": [
        "I am a bot created to let others get to know my creator better! Ask more questions, or visit the link to find out more :)"
      ],
      "link": "https://bennymai.me/"    // optional
    },

    ...

  ]
}

```

With Python 3.6+ installed, run the following commands in the root directory/envrionment:

```
pip3 install -r requirements.txt
python3 train.py
```

This model was trained using Python 3.9, PyTorch 1.7.1, and CUDA 11.0. If training is done on a supported GPU, Install the correct version of torch found [here](https://pytorch.org/get-started/locally/).

Or, find the download link for the correct `.whl` file from `https://download.pytorch.org/whl/torch_stable.html`

For example: `cu110/torch-1.7.1%2Bcu110-cp39-cp39-linux_x86_64.whl` is the correct file for Python 3.9, PyTorch 1.7.1, and CUDA 11.0, running on a Linux machine.

## Development

Deployed on Heroku using a Flask backend.

UI developed using HTML/CSS/Bootstrap

Support for fetching responses from a MongoDB database is WIP.
