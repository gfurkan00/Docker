FROM python:3.13-slim AS builder
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential libpq-dev \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /build
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

FROM python:3.13-slim
COPY --from=builder /install /usr/local
WORKDIR /app
COPY app.py .
EXPOSE 8080
CMD ["python", "app.py"]
