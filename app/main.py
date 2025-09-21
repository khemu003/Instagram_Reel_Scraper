from fastapi import FastAPI, HTTPException, Query
from app.scraper import fetch_reels

app = FastAPI()

@app.get("/scrape")
def scrape(username: str, limit: int = Query(10, gt=0, le=50)):
    try:
        reels = fetch_reels(username=username, limit=limit)
        return {"username": username, "reels": reels}
    except ValueError as ve:
        raise HTTPException(status_code=404, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {e}")
