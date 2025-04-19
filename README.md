# YouTube Video Scraper

This is a simple Python-based YouTube video scraper that extracts the titles and authors of the top 10 videos from a **YouTube search URL** (e.g., `https://www.youtube.com/results?search_query=tina+huang+ai+channel`) using the **YouTube Data API v3**.

## Features

- Accepts a YouTube search URL as input
- Extracts video titles and channel names from search results
- Saves results in `.txt`, `.csv`, or `.json` format
- Easy to run from the terminal

## Sample Output Files

- `yt_output.txt` – Plain text list of video titles and authors
- `yt_output.csv` – Structured CSV file with headers: `title`, `author`
- `yt_output.json` – JSON format for programmatic use

## Dependencies

Make sure you have the following Python packages installed:

- `google-api-python-client`
- `python-dotenv`

Install them using pip:

```bash
pip install google-api-python-client python-dotenv

Setup Instructions

1. Clone or download this repo into your desired directory.


2. Create a .env file in the same directory as main.py and add your YouTube API key:

YOUTUBE_API_KEY=your_api_key_here

You can get a YouTube Data API key by following instructions here:
https://developers.google.com/youtube/registering_an_application

3. Run the script from the terminal:
python main.py
4. Input the YouTube search URL when prompted. (Example:
https://www.youtube.com/results?search_query=tina+huang+ai+channel)
5. Choose a format to save results (txt, csv, or json), then provide a filename.
6. Your output will be saved in the chosen format (e.g., yt_output.txt, yt_output.csv).
Notes

The script only fetches the first 10 results from the YouTube search.

Ensure you have a working internet connection and a valid API key.

This tool is for educational and personal use only.
---
yt_scraper/
├── main.py         # Main Python script
├── yt_output.txt               # Output file with video titles & authors (plain text)
├── yt_output.csv               # Output file in CSV format
         yt_output.json
└── README.md             # Instructions or notes




