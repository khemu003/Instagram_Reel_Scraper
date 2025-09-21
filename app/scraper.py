import os
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()

APIFY_API_TOKEN = os.getenv("APIFY_API_TOKEN")

client = ApifyClient(APIFY_API_TOKEN)

def fetch_reels(username: str, limit: int = 10):
    input = {
        "username": [username],
        "resultsLimit": limit
    }
    actor = client.actor("apify/instagram-reel-scraper")
    run = actor.call(run_input=input)
    dataset_id = run["defaultDatasetId"]
    items = client.dataset(dataset_id).list_items().items
    reels = []
    for item in items:
        reels.append({
            "id": str(item.get("id", "")),
            "reel_url": item.get("url", ""),
            "video_url": item.get("videoUrl", ""),
            "thumbnail_url": item.get("images", [None])[0],
            "caption": item.get("caption", ""),
            "posted_at": item.get("timestamp", ""),
            "views": item.get("videoViewCount", 0),
            "likes": item.get("likesCount", 0),
            "comments": item.get("commentsCount", 0)
        })
    if not reels:
        raise ValueError("No reels found or user is private/non-existent.")
    return reels
