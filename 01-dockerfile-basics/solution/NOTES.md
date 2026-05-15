# Notes — solution

- **Why `COPY requirements.txt` before `COPY app.py`:** Docker caches each layer by the content hash of what it copies in. Putting rarely-changing things first means edits to app code don't bust the pip-install layer.
- **Why `--no-cache-dir` on pip:** pip otherwise saves wheels in `~/.cache/pip`, which would bloat the image with no benefit at runtime.
- **Why `ENTRYPOINT` + empty `CMD`:** with `ENTRYPOINT ["python", "app.py"]`, anything passed to `docker run` is appended as args. `CMD []` makes the default empty so the server runs normally.
- **`.dockerignore` is read by the daemon when assembling the build context.** Ignored files are never sent to the daemon at all — faster builds AND no accidental secrets baked in.
