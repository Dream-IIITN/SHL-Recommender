
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from SHLAdvancedRecommender import SHLAdvancedRecommender
# import os
# import sys  # Make sure to import sys if used in SHLAdvancedRecommender

# app = FastAPI()

# # Initialize recommender
# try:
#     recommender = SHLAdvancedRecommender()
# except Exception as e:
#     recommender = None
#     print(f"Failed to initialize SHLAdvancedRecommender: {e}")

# class QueryRequest(BaseModel):
#     text: str
#     language: str
#     job_level: str
#     Completion_time : int


# @app.post("/recommend")
# async def get_recommendations(request: QueryRequest):
#     if recommender is None:
#         raise HTTPException(status_code=500, detail="Recommender not initialized")
    
#     try:
#         results = recommender.recommend_solution(
#             user_query=request.text,
#             user_language=request.language
#         )
#         return {
#             "query": request.text,
#             "sources": results.get("sources", [])
#         }
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# @app.get("/health")
# async def health_check():
#     return {"status": "healthy"}

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from SHLAdvancedRecommender import SHLAdvancedRecommender
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# CORS Middleware for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=[""],  # Replace "*" with frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize recommender
try:
    recommender = SHLAdvancedRecommender()
    logger.info("SHLAdvancedRecommender initialized successfully.")
except Exception as e:
    recommender = None
    logger.error(f"Failed to initialize SHLAdvancedRecommender: {e}")

# Request schema
class QueryRequest(BaseModel):
    text: str = Field(..., min_length=5, description="The query text")
    language: str = Field(..., regex="^(en|fr|de|es)$", description="Supported language codes")
    job_level: str = Field(..., description="User job level, e.g. 'Entry', 'Mid', 'Senior'")
    completion_time: int = Field(..., gt=0, le=120, description="Expected completion time in minutes")

# API endpoint
@app.post("/recommend")
async def get_recommendations(request: QueryRequest):
    if recommender is None:
        raise HTTPException(status_code=500, detail="Recommender not initialized")
    
    try:
        results = recommender.recommend_solution(
            user_query=request.text,
            user_language=request.language,
            job_level=request.job_level,
            completion_time=request.completion_time
        )
        return {
            "query": request.text,
            "sources": results.get("sources", [])
        }
    except Exception as e:
        logger.exception("Recommendation generation failed.")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Entry point for local run
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
