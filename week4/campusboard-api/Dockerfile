# -- Stage 1: Builder --
FROM python:3.12-slim AS builder

WORKDIR /app

#Create a virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

#Install dependencies first (better layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir --upgrade -r requirements.txt

#------ Stage 2: Runtime ---
FROM python:3.12-slim AS runtime

# Create non-roor user for security
RUN groupadd -r addgroup && useradd -r -g addgroup appuser

WORKDIR /app

#COPY only venv
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

#Copy application code
COPY --chown=appuser:appgroup app/ ./app/

USER appuser

EXPOSE 8080

# Use exec form so signals reach uvicorn properly
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
