import os
import json
import csv
from googleapiclient.discovery import build
from urllib.parse import urlparse, parse_qs
from dotenv import load_dotenv

load_dotenv()  
api_key = os.getenv("YOUTUBE_API_KEY")
youtube = build("youtube", "v3", developerKey=api_key)

# Modify this function to handle search query URLs
def extract_search_query(url):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    if "search_query" in query_params:
        return query_params["search_query"][0]
    else:
        raise Exception("Unsupported URL format or missing search query.")

# Modify this function to search videos based on the search query
def fetch_titles(query):
    # Use the search query to fetch video results
    search_response = youtube.search().list(
        q=query, 
        part="snippet", 
        type="video", 
        maxResults=10
    ).execute()

    results = []
    for item in search_response["items"]:
        title = item["snippet"]["title"]
        author = item["snippet"]["channelTitle"]
        results.append({"title": title, "author": author})
        print(f"{title} — by {author}")
    return results

def save_results(data, format_choice, filename):
    if format_choice == "txt":
        with open(filename, "w", encoding="utf-8") as f:
            for entry in data:
                f.write(f"{entry['title']} — by {entry['author']}\n")
    elif format_choice == "csv":
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["title", "author"])
            writer.writeheader()
            writer.writerows(data)
    elif format_choice == "json":
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
    else:
        print("Unsupported file format.")

if __name__ == "__main__":
    url = input("Enter YouTube search URL: ")
    search_query = extract_search_query(url)
    videos = fetch_titles(search_query)

    format_choice = input("Save as (txt, csv, json): ").strip().lower()
    filename = input(f"Enter output filename (without extension): ").strip() + f".{format_choice}"
    save_results(videos, format_choice, filename)
    print(f"Saved to {filename}")
