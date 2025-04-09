# Updated Dockerfile
FROM python:3.10-slim-bullseye

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    TRANSFORMERS_CACHE=/app/.cache \
    CHROMA_CACHE_DIR=/app/.chroma_cache \
    SQLITE3_LIB=/usr/lib

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libsqlite3-dev \
    && rm -rf /var/lib/apt/lists/*

# Create cache directories and set permissions
WORKDIR /app
RUN mkdir -p /app/.cache /app/.chroma_cache && \
    chmod -R 755 /app/.cache /app/.chroma_cache

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir pysqlite3-binary

# Pre-download models with validation
RUN python -c "from sentence_transformers import SentenceTransformer; \
    model = SentenceTransformer('all-MiniLM-L6-v2'); \
    model.encode('test text')"

# Create non-root user and transfer ownership
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

# Copy application files
COPY . .

# Start command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]