# News App

A simple Python script that fetches and displays the latest news headlines using the NewsAPI service.

## Description

This project demonstrates how to query the NewsAPI, parse JSON responses, and display a list of news articles in the terminal.

## Features

- Fetches recent news articles based on a user search query
- Uses the NewsAPI `everything` endpoint
- Displays article titles and URLs in the terminal
- Handles API errors gracefully

## Requirements

- Python 3.x
- `requests` Python package
- NewsAPI API key

## Installation

1. Install Python 3 if needed.
2. Install the required Python package:

```bash
pip install requests
```

## Configuration

The script currently includes a NewsAPI key inside `NewsApp.py`:

```python
api = "2e59ee9159a14863987e30bfa10109a7"
```

For security and reliability, replace this key with your own NewsAPI key from https://newsapi.org.

## Usage

Run the script from the project folder:

```bash
python NewsApp.py
```

Then enter the topic or keyword you want to search for when prompted.

Example:

```text
What type of news are you interested in today? technology
```

The script will display the latest matching article titles and URLs.

## Project Structure

- `NewsApp.py` - main Python script for fetching and displaying news.

## Notes

- This script uses NewsAPI and is subject to NewsAPI usage limits.
- The current query fetches articles from the last 30 days.
- If no articles are found, the script reports that no results were returned.
