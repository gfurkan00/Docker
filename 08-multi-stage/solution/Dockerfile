# ----- Build stage: has gcc, libffi, etc. -----
FROM python:3.13-slim AS builder

# Build tools needed by cryptography / cffi.
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        libffi-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /build
COPY requirements.txt .

# Install into a stand-alone prefix so we can copy only that into the runtime.
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# ----- Runtime stage: tiny, no build tools -----
FROM python:3.13-slim

# Copy installed Python packages from the builder.
COPY --from=builder /install /usr/local

WORKDIR /app
COPY app.py .

EXPOSE 8080
CMD ["python", "app.py"]
