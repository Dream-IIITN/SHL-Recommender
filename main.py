
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from SHLAdvancedRecommender import SHLAdvancedRecommender
import os
import sys  # Make sure to import sys if used in SHLAdvancedRecommender

app = FastAPI()

# Initialize recommender
try:
    recommender = SHLAdvancedRecommender()
except Exception as e:
    recommender = None
    print(f"Failed to initialize SHLAdvancedRecommender: {e}")

class QueryRequest(BaseModel):
    text: str
    language: str
    job_level: str
    Completion_time : int


@app.post("/recommend")
async def get_recommendations(request: QueryRequest):
    if recommender is None:
        raise HTTPException(status_code=500, detail="Recommender not initialized")
    
    try:
        results = recommender.recommend_solution(
            user_query=request.text,
            user_language=request.language
        )
        return {
            "query": request.text,
            "sources": results.get("sources", [])
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
