# Use Python
FROM python:3.11-slim

# Workdir at repo root
WORKDIR /app

# Install deps first (better caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Make sure Python imports from the inner app/ folder
ENV PYTHONPATH=/app/app

# Run from the inner app folder so "main:app" is clear
WORKDIR /app/app

# Start FastAPI (no package prefix needed now)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
