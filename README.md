# Instagram Reel Scraper API

Fast REST API to scrape Instagram reels for a given username (public profiles only).

## About

This project provides a lightweight and efficient REST API built with Python to scrape Instagram reels from public profiles. It allows users to fetch reel video URLs and metadata without needing Instagram login credentials or official API access.

## Features

- Scrape Instagram reels videos and metadata using a username
- Supports only public Instagram profiles
- No login or authentication needed
- Simple REST API interface for easy integration
- Fast and lightweight Python implementation
- Docker support included for easy deployment

## Getting Started

### Prerequisites

- Python 3.8+
- Docker (optional, for containerized deployment)

### Initialize Project with uv

```
uv init
```

### Setting up Virtual Environment

It is highly recommended to use a Python virtual environment to manage dependencies and avoid package conflicts.

Create a virtual environment in your project directory:

```

uv venv

```

Activate the virtual environment:

- On Windows:

```

.venv\Scripts\activate

```

After activation, install the dependencies:

```

uv add -r requirements.txt

```

To deactivate the virtual environment, simply run:

```

deactivate

```

### Installation

Clone the repository:

```

git clone https://github.com/khemu003/Instagram_Reel_Scraper.git
cd Instagram_Reel_Scraper

```

Follow the virtual environment setup above before installing dependencies.

### Running the API

Run the API server locally:

```
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

Or build and run with Docker:

```

docker build -t instagram-reel-scraper .
docker run -p 8000:8000 instagram-reel-scraper

```

## API Endpoints

- `GET /reels/{username}`

  Fetch Instagram reels for the given public username.

  Example Request:

```

curl.exe -X GET "http://127.0.0.1:8000/scrape?username=user_name&limit=5" -H "accept: application/json"

```

Example Response:

```
{
  "username": "regexsoftware",
  "reels": [
    {
      "id": ,
      "reel_url": ,
      "video_url": ,
      "thumbnail_url": ,
      "caption": ,
      "posted_at": ,
      "views": ,
      "likes": ,
      "comments": 
    }
  ]
}

```

## Contact

For any questions or suggestions, please open an issue in this repository.
```
