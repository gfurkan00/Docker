# Slim Python base — small and well maintained.
FROM python:3.13-slim

# Set a clear working directory; all later paths are relative to it.
WORKDIR /app

# Dependencies first: this layer only invalidates when requirements.txt changes.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Source code last: editing app.py only invalidates this layer onward.
COPY app.py .

# Document the listening port (does not actually publish it).
EXPOSE 8080

# ENTRYPOINT is the fixed program; CMD is the default (overridable) argument list.
# This combo lets `docker run image --help` forward `--help` to python app.py.
ENTRYPOINT ["python", "app.py"]
CMD []
