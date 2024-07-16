from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import sqlite3
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from any origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all HTTP headers
)

# Define the data model for the response
class NewsItem(BaseModel):
    date: str
    title: str
    url: str
    image: str
    source: str
    favicon: Optional[str]  # Allow None values
    body: str

def get_random_news(limit: int):
    conn = sqlite3.connect('news.db')
    cursor = conn.cursor()
    
    # Fetch up to `limit` random news items sorted by date in descending order
    cursor.execute('''
        SELECT date, title, url, image, source, favicon, body 
        FROM news 
        ORDER BY RANDOM() 
        LIMIT ?
    ''', (limit,))
    rows = cursor.fetchall()
    conn.close()
    
    # Convert rows to list of dictionaries
    news_list = [
        {
            "date": row[0],
            "title": row[1],
            "url": row[2],
            "image": row[3],
            "source": row[4],
            "favicon": row[5] if row[5] is not None else '',  # Ensure `favicon` is not None
            "body": row[6]
        }
        for row in rows
    ]
    
    # Sort news items by date in descending order
    news_list.sort(key=lambda x: x['date'], reverse=True)
    
    return news_list

@app.get("/news", response_model=List[NewsItem])
async def get_news(limit: int = 200):
    if limit <= 0 or limit > 200:
        raise HTTPException(status_code=400, detail="Limit must be between 1 and 200")
    news_list = get_random_news(limit)
    return news_list

# If you need to run the FastAPI app, use the following command:
# uvicorn main:app --reload
