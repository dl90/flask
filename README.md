# Apple Music Clone
[![License](https://img.shields.io/npm/l/next.svg?style=for-the-badge&labelColor=000000)](LICENSE.md)

## Getting Started (pip)
Install dependencies
``` bash
pip install flask

```

Run
``` bash
python3 app.py

```


## Getting Started ([Poetry](https://github.com/python-poetry/poetry))
Install dependencies
``` bash
poetry install
```

Run
``` bash
poetry run python app.py
```


## Incomplete Features
- Persist client data
  - Since music playback and data fetching from YouTube occurs on the client, we will implement data persistence for play history and search history by passing data from the client to the server
  - The server will store the received data within the SQLite database

## Different Branch
Didn't get a chance to merge branch Don due to too many conflicts and structure change.

## Credentials
Enter your APIKEY and CLIENTID for the YouTube Data API from Google Cloud Console into [`static/scripts/player.js`](static/scripts/player.js)
