# Docker Learning Roadmap Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a 10-challenge, folder-based Docker learning roadmap (English) at the repo root, each challenge with `README.md`, `starter/`, `solution/`, plus a top-level `README.md` and `RESOURCES.md`.

**Architecture:** Static content repository. Each numbered folder is a self-contained challenge. Starters are deliberately incomplete (no Dockerfile / no compose). Solutions are runnable reference answers. A shared Flask scaffold keeps app code minimal so cognitive load stays on Docker.

**Tech Stack:** Markdown, Python 3.13 + Flask, PostgreSQL 16, Redis 7, Nginx (final challenge only), Docker Engine + Compose v2.

**Spec:** `docs/superpowers/specs/2026-05-15-docker-learning-roadmap-design.md`

**Verification model:** This is content, not code — no unit tests. "Verification" for each challenge means: running `docker compose up` (or `docker build && docker run`) on the `solution/` and checking the success criteria from the spec produce the expected output. These runs happen during execution and are documented in Task 12 (smoke test sweep).

**Git workflow:**
- All work happens inside a git worktree (per user's global workflow). Worktree creation is handled by the `using-git-worktrees` skill before executing this plan.
- Branch name: `feature/docker-learning-roadmap`.
- One commit per task, Conventional Commits style.
- Final task opens a PR via `gh pr create`.

---

## File Structure (created by this plan)

```
Docker/
├── README.md                          # OVERWRITE — roadmap index
├── RESOURCES.md                       # CREATE
├── 01-dockerfile-basics/
│   ├── README.md
│   ├── starter/{app.py,requirements.txt,.dockerignore.example}
│   └── solution/{Dockerfile,.dockerignore,app.py,requirements.txt,NOTES.md}
├── 02-run-deep-dive/
│   ├── README.md
│   ├── starter/{app.py,requirements.txt,Dockerfile}
│   └── solution/{commands.md,NOTES.md}
├── 03-volumes/
│   ├── README.md
│   ├── starter/{app.py,requirements.txt}
│   └── solution/{compose.yaml,app.py,requirements.txt,NOTES.md}
├── 04-networks/
│   ├── README.md
│   ├── starter/{app.py,requirements.txt}
│   └── solution/{Dockerfile,app.py,requirements.txt,commands.md,NOTES.md}
├── 05-compose-intro/
│   ├── README.md
│   ├── starter/{app.py,requirements.txt,Dockerfile}
│   └── solution/{compose.yaml,app.py,requirements.txt,Dockerfile,NOTES.md}
├── 06-compose-realistic/
│   ├── README.md
│   ├── starter/{app.py,requirements.txt,Dockerfile,initdb.d/01_schema.sql}
│   └── solution/{compose.yaml,app.py,requirements.txt,Dockerfile,initdb.d/01_schema.sql,NOTES.md}
├── 07-dev-workflow/
│   ├── README.md
│   ├── starter/{app.py,requirements.txt,Dockerfile,compose.yaml}
│   └── solution/{Dockerfile,compose.yaml,compose.override.yaml,app.py,requirements.txt,NOTES.md}
├── 08-multi-stage/
│   ├── README.md
│   ├── starter/{app.py,requirements.txt}
│   └── solution/{Dockerfile,app.py,requirements.txt,NOTES.md}
├── 09-env-and-secrets/
│   ├── README.md
│   ├── starter/{app.py,requirements.txt,Dockerfile,compose.yaml}
│   └── solution/{compose.yaml,.env.example,.gitignore,app.py,requirements.txt,Dockerfile,NOTES.md}
├── 10-final-challenge/
│   ├── README.md
│   ├── starter/{api/,worker/,proxy/}
│   └── solution/{compose.yaml,compose.override.yaml,.env.example,api/,worker/,db/initdb.d/,proxy/,NOTES.md}
└── docs/superpowers/                  # plan & spec already here, untouched
```

**Leave alone:** `example1/`, `usefull commands.md`, `.codex`, existing `.git/`.

---

## Shared Conventions

### Challenge README template

Every `0X-name/README.md` uses these sections, in this order, with these exact H2 headers:

```markdown
# Challenge 0X — <Title>

## Goal
One paragraph: what you will be able to do after this challenge.

## Concepts introduced
- Bullet list of new Docker concepts (e.g. layer caching, named volumes).

## The challenge
Concrete task. Describe what's in `starter/` and what you must produce.

## Success criteria
Verifiable checks. Use a checkbox list with concrete commands and expected output.

## Hints
1. First hint (gentle nudge).
2. Second hint (more direct).
3. Third hint (almost the answer).

## Reference
- Link to relevant Docker docs page(s).
```

### Shared Flask scaffold (reused, with small variations, in many challenges)

`app.py` base (do NOT inline anywhere yet, copy from here):

```python
from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    name = os.environ.get("NAME", "World")
    return f"<h1>Hello, {name}!</h1>"

@app.route("/health")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "8080")))
```

`requirements.txt` base:

```
flask==3.0.3
```

Challenge-specific apps extend this scaffold (e.g. add `redis`, `psycopg[binary]`).

---

## Task 1: Repo scaffolding (root README, RESOURCES.md, empty challenge folders)

**Files:**
- Modify: `README.md` (overwrite the 1-line existing file)
- Create: `RESOURCES.md`
- Create: empty directories `01-dockerfile-basics/` through `10-final-challenge/`

- [ ] **Step 1: Create all 10 empty challenge directories**

```bash
cd <repo-root>
mkdir -p 01-dockerfile-basics/{starter,solution} \
         02-run-deep-dive/{starter,solution} \
         03-volumes/{starter,solution} \
         04-networks/{starter,solution} \
         05-compose-intro/{starter,solution} \
         06-compose-realistic/{starter,solution} \
         07-dev-workflow/{starter,solution} \
         08-multi-stage/{starter,solution} \
         09-env-and-secrets/{starter,solution} \
         10-final-challenge/{starter,solution}
```

- [ ] **Step 2: Overwrite root `README.md`**

Replace existing contents with:

```markdown
# Docker — Hands-on Learning Roadmap

A challenge-driven path from Dockerfile basics to a realistic multi-container dev stack. Every folder is a problem to solve, not a tutorial to copy.

## How to use

1. Pick the lowest-numbered challenge you haven't finished.
2. Read its `README.md`.
3. Work inside `starter/` — write the Dockerfile / `compose.yaml` yourself.
4. Verify against the **Success criteria** in the README.
5. Only when you're done (or truly stuck after the hints), peek at `solution/`.

## Challenges

| # | Folder | Focus |
|---|---|---|
| 01 | [`01-dockerfile-basics/`](./01-dockerfile-basics/) | Layer caching, `.dockerignore`, `ENTRYPOINT` vs `CMD` |
| 02 | [`02-run-deep-dive/`](./02-run-deep-dive/) | `docker run` flags, `exec`, `logs`, lifecycle |
| 03 | [`03-volumes/`](./03-volumes/) | Bind mounts vs named volumes, data persistence |
| 04 | [`04-networks/`](./04-networks/) | User-defined bridges, DNS between containers |
| 05 | [`05-compose-intro/`](./05-compose-intro/) | First `compose.yaml`: web + Redis |
| 06 | [`06-compose-realistic/`](./06-compose-realistic/) | Healthchecks, `depends_on` conditions, init scripts |
| 07 | [`07-dev-workflow/`](./07-dev-workflow/) | `compose.override.yaml`, hot reload, debugger |
| 08 | [`08-multi-stage/`](./08-multi-stage/) | Builder stage, slim runtime images |
| 09 | [`09-env-and-secrets/`](./09-env-and-secrets/) | `.env`, `env_file`, dev-grade secret handling |
| 10 | [`10-final-challenge/`](./10-final-challenge/) | API + worker + DB + cache + Nginx |

## Prerequisites

- Docker Engine 24+ and Docker Compose v2 (`docker compose version`).
- Python 3 basic knowledge (the example apps are small Flask services).
- A terminal you're comfortable in.

## See also

- [`RESOURCES.md`](./RESOURCES.md) — curated external resources.
- [`usefull commands.md`](./usefull%20commands.md) — cheat sheet of common Docker commands.
- [`example1/`](./example1/) — the original throwaway sample (kept for reference).
```

- [ ] **Step 3: Create `RESOURCES.md`**

```markdown
# Docker — Curated Resources

Quality over quantity. Five great resources beat fifty mediocre ones.

## Official documentation

- [Docker docs — Get started](https://docs.docker.com/get-started/) — the canonical entry point.
- [Dockerfile reference](https://docs.docker.com/reference/dockerfile/) — every instruction explained.
- [Compose file reference](https://docs.docker.com/reference/compose-file/) — the full v2 spec.
- [Networking overview](https://docs.docker.com/engine/network/) — bridge, host, overlay, DNS.
- [Storage overview](https://docs.docker.com/engine/storage/) — volumes, bind mounts, tmpfs.

## Free interactive

- [Play with Docker](https://labs.play-with-docker.com/) — a free, browser-based Docker playground (no local install needed).
- [Docker's own tutorials](https://docs.docker.com/guides/) — short, focused, official.

## Books

- *Docker Deep Dive* — Nigel Poulton. The clearest end-to-end book; updated regularly.

## Video

- [TechWorld with Nana — Docker Tutorial for Beginners](https://www.youtube.com/watch?v=3c-iBn73dDE) — best single-video visual overview.

## Cheat sheet

- [`usefull commands.md`](./usefull%20commands.md) in this repo.
```

- [ ] **Step 4: Verify structure**

Run:
```bash
ls -la
find . -maxdepth 2 -type d -name 'starter' -o -name 'solution' | sort
```

Expected: `README.md` and `RESOURCES.md` listed in root; 20 lines total from `find` (10 challenges × 2 subfolders).

- [ ] **Step 5: Commit**

```bash
git add README.md RESOURCES.md 01-*/ 02-*/ 03-*/ 04-*/ 05-*/ 06-*/ 07-*/ 08-*/ 09-*/ 10-*/
git commit -m "feat: scaffold roadmap structure (root README, resources, empty challenges)"
```

---

## Task 2: Challenge 01 — Dockerfile basics

**Files:**
- Create: `01-dockerfile-basics/README.md`
- Create: `01-dockerfile-basics/starter/{app.py,requirements.txt,.dockerignore.example}`
- Create: `01-dockerfile-basics/solution/{Dockerfile,.dockerignore,app.py,requirements.txt,NOTES.md}`

- [ ] **Step 1: Create `starter/app.py`**

```python
from flask import Flask
import os, sys

app = Flask(__name__)

@app.route("/")
def hello():
    name = os.environ.get("NAME", "World")
    return f"<h1>Hello, {name}!</h1>"

@app.route("/health")
def health():
    return {"status": "ok"}, 200

def print_help():
    print("Usage: docker run <image> [--help]")
    print("Env vars: NAME (default: World), PORT (default: 8080)")

if __name__ == "__main__":
    if "--help" in sys.argv:
        print_help()
        sys.exit(0)
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "8080")))
```

- [ ] **Step 2: Create `starter/requirements.txt`**

```
flask==3.0.3
```

- [ ] **Step 3: Create `starter/.dockerignore.example`**

Empty file with a single comment line so the learner knows the concept exists but has to author the real one:

```
# Rename this file to `.dockerignore` and fill it in with patterns
# that should NOT be copied into the image.
```

- [ ] **Step 4: Create `README.md` using the template from Shared Conventions**

```markdown
# Challenge 01 — Dockerfile basics

## Goal
Build a small Flask image that rebuilds quickly when only source code changes, ignores junk files from the build context, and accepts a CLI flag.

## Concepts introduced
- Layer caching and how `COPY` ordering affects it.
- `.dockerignore` and why it matters (build speed, image hygiene, secrets).
- `WORKDIR`, `COPY` vs `ADD`.
- `ENTRYPOINT` + `CMD` so the container can accept extra args.

## The challenge
Inside `starter/` you have a Flask app and a `requirements.txt`. Write a `Dockerfile` and a `.dockerignore` so that:

1. The first `docker build` succeeds and the resulting image runs the app on port 8080.
2. After the first build, editing only `app.py` and rebuilding does **not** reinstall pip dependencies.
3. Running the container with the extra arg `--help` prints usage instead of starting the server.
4. The image does not contain `__pycache__/`, `.git/`, local virtualenvs (`.venv/`, `venv/`), or any `.dockerignore.example` artifact.

## Success criteria
- [ ] `docker build -t ch01 .` succeeds.
- [ ] `docker run --rm -p 8080:8080 ch01` serves `http://localhost:8080` and returns the greeting.
- [ ] `docker run --rm ch01 --help` prints the usage and exits 0.
- [ ] After touching `app.py`, `docker build -t ch01 .` finishes in under 5 seconds (use the cache).
- [ ] `docker run --rm ch01 ls -la /app` shows no `__pycache__` or `.git`.
- [ ] `docker image inspect ch01 --format '{{.Size}}'` returns a size below 150 MB.

## Hints
1. Order matters: which `COPY` should come first, dependencies or source code?
2. `ENTRYPOINT ["python", "app.py"]` plus an empty `CMD []` lets `--help` be appended as an argument.
3. `.dockerignore` works exactly like `.gitignore` — list every directory you don't want in the build context.

## Reference
- https://docs.docker.com/build/cache/
- https://docs.docker.com/build/concepts/context/#dockerignore-files
- https://docs.docker.com/reference/dockerfile/#entrypoint
```

- [ ] **Step 5: Create `solution/Dockerfile`**

```dockerfile
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
```

- [ ] **Step 6: Create `solution/.dockerignore`**

```
.git/
.gitignore
.venv/
venv/
__pycache__/
*.pyc
*.pyo
.dockerignore.example
Dockerfile
README.md
NOTES.md
```

- [ ] **Step 7: Copy `starter/app.py` and `starter/requirements.txt` to `solution/`**

```bash
cp 01-dockerfile-basics/starter/app.py        01-dockerfile-basics/solution/app.py
cp 01-dockerfile-basics/starter/requirements.txt 01-dockerfile-basics/solution/requirements.txt
```

- [ ] **Step 8: Create `solution/NOTES.md`**

```markdown
# Notes — solution

- **Why `COPY requirements.txt` before `COPY app.py`:** Docker caches each layer by the content hash of what it copies in. Putting rarely-changing things first means edits to app code don't bust the pip-install layer.
- **Why `--no-cache-dir` on pip:** pip otherwise saves wheels in `~/.cache/pip`, which would bloat the image with no benefit at runtime.
- **Why `ENTRYPOINT` + empty `CMD`:** with `ENTRYPOINT ["python", "app.py"]`, anything passed to `docker run` is appended as args. `CMD []` makes the default empty so the server runs normally.
- **`.dockerignore` is read by the daemon when assembling the build context.** Ignored files are never sent to the daemon at all — faster builds AND no accidental secrets baked in.
```

- [ ] **Step 9: Smoke-build the solution**

Run from `01-dockerfile-basics/solution/`:
```bash
docker build -t ch01-solution .
docker run --rm ch01-solution --help
```
Expected: build succeeds; `--help` invocation prints usage and exits.

- [ ] **Step 10: Commit**

```bash
git add 01-dockerfile-basics
git commit -m "feat(01): dockerfile basics challenge + solution"
```

---

## Task 3: Challenge 02 — Run deep-dive

**Files:**
- Create: `02-run-deep-dive/README.md`
- Create: `02-run-deep-dive/starter/{app.py,requirements.txt,Dockerfile}` (reuse Challenge 01 solution)
- Create: `02-run-deep-dive/solution/{commands.md,NOTES.md}`

- [ ] **Step 1: Copy Challenge 01 solution files into `starter/`**

```bash
cp 01-dockerfile-basics/solution/{app.py,requirements.txt,Dockerfile,.dockerignore} 02-run-deep-dive/starter/
```

- [ ] **Step 2: Create `README.md`**

```markdown
# Challenge 02 — docker run deep-dive

## Goal
Become fluent with the most common `docker run` flags and container lifecycle commands. No more copy-paste from Stack Overflow.

## Concepts introduced
- `-p` (publish) vs `-P` (publish-all-random).
- `-d` (detached) vs foreground vs `-it` (interactive + TTY).
- `--rm`, `--name`, `--restart`.
- `docker exec`, `docker logs -f`, `docker stop` vs `docker kill`.

## The challenge
You have a working image (`starter/` reuses Challenge 01's solution). Without writing any new code, produce a `commands.md` that contains the exact `docker` commands to:

1. Build the image as `ch02`.
2. Run it in the **foreground** with port 8080 mapped, name `ch02-fg`, and auto-removed on exit.
3. Run it in the **background** with port 8081 mapped, name `ch02-bg`, restart policy `unless-stopped`.
4. Stream the logs of `ch02-bg` live.
5. Open an interactive `sh` inside the running `ch02-bg` and `cat /app/app.py` from inside.
6. Stop `ch02-bg` gracefully, then remove it.
7. Show the difference in observable behaviour between `docker stop` and `docker kill` for this image (one sentence each).

## Success criteria
- [ ] `commands.md` is filled in with runnable commands; copy-pasting each in order works end to end.
- [ ] `curl localhost:8080` works during step 2.
- [ ] `curl localhost:8081` works during step 3.
- [ ] `docker logs -f ch02-bg` shows new lines when you `curl` it.
- [ ] You can explain in your own words when you'd use `-d` vs foreground.

## Hints
1. `--rm` removes the container on exit but is incompatible with `--restart`.
2. `docker exec -it <name> sh` opens an interactive shell inside a running container.
3. `docker stop` sends SIGTERM (graceful, 10s grace period). `docker kill` sends SIGKILL (immediate, no cleanup).

## Reference
- https://docs.docker.com/reference/cli/docker/container/run/
- https://docs.docker.com/reference/cli/docker/container/exec/
- https://docs.docker.com/engine/containers/start-containers-automatically/
```

- [ ] **Step 3: Create `solution/commands.md`**

```markdown
# Solution — challenge 02 commands

```bash
# 1. Build
docker build -t ch02 .

# 2. Foreground, auto-removed
docker run --rm --name ch02-fg -p 8080:8080 ch02
# (Ctrl-C to stop; the container is removed automatically.)

# 3. Background, restart policy
docker run -d --name ch02-bg -p 8081:8081 -e PORT=8081 \
  --restart unless-stopped ch02

# 4. Follow logs
docker logs -f ch02-bg

# 5. Interactive shell inside
docker exec -it ch02-bg sh
# inside: cat /app/app.py ; exit

# 6. Graceful stop + remove
docker stop ch02-bg
docker rm ch02-bg
```

## stop vs kill (one-liners)

- `docker stop`: sends SIGTERM, gives the process 10s to clean up, then SIGKILL. Flask logs a shutdown line.
- `docker kill`: sends SIGKILL immediately. No shutdown line, no graceful cleanup.
```

- [ ] **Step 4: Create `solution/NOTES.md`**

```markdown
# Notes — solution

- **`--rm` + `--restart`:** mutually exclusive. `--rm` means "delete on exit"; `--restart` means "bring it back if it exits". Docker rejects both together.
- **`-d` vs foreground:** detached is for "set and forget" runs (services). Foreground is for development and debugging — you see stdout immediately and Ctrl-C kills it.
- **`-it`:** `-i` keeps STDIN open, `-t` allocates a TTY. Both are needed for an interactive shell. Without `-t`, prompts don't render. Without `-i`, you can't type.
- **`docker logs -f`** is your default debugging tool. Add `--tail 100` to start from the recent past.
```

- [ ] **Step 5: Smoke-run the solution**

```bash
cd 02-run-deep-dive/starter
docker build -t ch02 .
docker run -d --name ch02-bg -p 8081:8081 -e PORT=8081 ch02
curl -s localhost:8081/health
docker stop ch02-bg && docker rm ch02-bg
```
Expected: `{"status":"ok"}` from `curl`; clean stop/remove.

- [ ] **Step 6: Commit**

```bash
git add 02-run-deep-dive
git commit -m "feat(02): run deep-dive challenge + solution"
```

---

## Task 4: Challenge 03 — Volumes

**Files:**
- Create: `03-volumes/README.md`
- Create: `03-volumes/starter/{app.py,requirements.txt}`
- Create: `03-volumes/solution/{compose.yaml,app.py,requirements.txt,NOTES.md}`

- [ ] **Step 1: Create `starter/app.py`**

```python
from flask import Flask, jsonify
import os, psycopg
from psycopg.rows import dict_row

app = Flask(__name__)

DSN = (
    f"host={os.environ['DB_HOST']} "
    f"port={os.environ.get('DB_PORT', '5432')} "
    f"dbname={os.environ['DB_NAME']} "
    f"user={os.environ['DB_USER']} "
    f"password={os.environ['DB_PASSWORD']}"
)

def init_db():
    with psycopg.connect(DSN) as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS notes (id SERIAL PRIMARY KEY, text TEXT)")
        conn.commit()

@app.route("/notes", methods=["GET"])
def list_notes():
    with psycopg.connect(DSN, row_factory=dict_row) as conn:
        rows = conn.execute("SELECT id, text FROM notes ORDER BY id").fetchall()
        return jsonify(rows)

@app.route("/notes/<text>", methods=["POST"])
def add_note(text):
    with psycopg.connect(DSN) as conn:
        conn.execute("INSERT INTO notes (text) VALUES (%s)", (text,))
        conn.commit()
    return {"ok": True}, 201

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=8080)
```

- [ ] **Step 2: Create `starter/requirements.txt`**

```
flask==3.0.3
psycopg[binary]==3.2.3
```

- [ ] **Step 3: Create `README.md`**

```markdown
# Challenge 03 — Volumes

## Goal
Understand the three kinds of mounts (anonymous, named, bind) and when each one is the right tool. Make Postgres data survive `docker rm`.

## Concepts introduced
- Anonymous volume vs **named volume** vs **bind mount**.
- Where data lives on the host for each kind.
- Editing source code on the host and seeing changes in the container (bind mount).
- Permission gotchas (UID/GID inside container vs on host).

## The challenge
The `starter/` Flask app stores notes in Postgres. Using **either** raw `docker` commands **or** a small `compose.yaml`, set things up so that:

1. Postgres runs in its own container and Flask connects to it.
2. Postgres data lives in a **named volume**: destroying and recreating the Postgres container preserves all notes.
3. The Flask source code is **bind-mounted** from the host, so editing `app.py` and restarting Flask picks up the change without rebuilding the image.

You may use the official `postgres:16-alpine` image and write a tiny `Dockerfile` for Flask (or reuse the pattern from Challenge 01).

## Success criteria
- [ ] `POST /notes/hello` adds a note; `GET /notes` returns it.
- [ ] `docker rm -f <postgres-container>` followed by recreating it (against the same named volume) still returns the previous notes.
- [ ] Editing `app.py` on the host changes the response after a Flask restart (no rebuild needed).
- [ ] `docker volume ls` lists the named volume; `docker volume inspect <name>` shows a `Mountpoint` on the host.

## Hints
1. Named volume syntax: `-v pgdata:/var/lib/postgresql/data` (or `volumes:` in compose).
2. Bind mount syntax: `-v "$(pwd)/app.py:/app/app.py"` mounts a single file; `-v "$(pwd):/app"` mounts the whole directory.
3. Postgres connection envs needed by the starter: `DB_HOST`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`.

## Reference
- https://docs.docker.com/engine/storage/volumes/
- https://docs.docker.com/engine/storage/bind-mounts/
```

- [ ] **Step 4: Copy starter app files into `solution/`**

```bash
cp 03-volumes/starter/{app.py,requirements.txt} 03-volumes/solution/
```

- [ ] **Step 5: Create `solution/compose.yaml`**

```yaml
services:
  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: notes
      POSTGRES_USER: notes
      POSTGRES_PASSWORD: notes
    volumes:
      - pgdata:/var/lib/postgresql/data   # NAMED volume — survives container removal
    ports:
      - "5432:5432"                       # exposed for host-side debugging only

  web:
    image: python:3.13-slim
    working_dir: /app
    volumes:
      - ./:/app                           # BIND mount — host source = container source
    command: sh -c "pip install --no-cache-dir -r requirements.txt && python app.py"
    environment:
      DB_HOST: db
      DB_NAME: notes
      DB_USER: notes
      DB_PASSWORD: notes
    ports:
      - "8080:8080"
    depends_on:
      - db

volumes:
  pgdata:
```

- [ ] **Step 6: Create `solution/NOTES.md`**

```markdown
# Notes — solution

- **Why a named volume for Postgres:** the Postgres image writes data to `/var/lib/postgresql/data`. Without a volume, that directory lives in the container's writable layer and dies with `docker rm`. A named volume is managed by Docker (so you don't pick the host path), and survives container deletion.
- **Why a bind mount for the source:** during learning/dev you want edits on the host to show up instantly in the container. The trade-off: the path is host-specific and the file system perms are shared with the host.
- **Anonymous volumes** (`-v /var/lib/postgresql/data` with no name) work for persistence within a single `up`/`down` cycle but produce volumes with random names that pile up — avoid them.
- **Demo of persistence:**
  ```bash
  docker compose up -d
  curl -X POST localhost:8080/notes/first
  docker compose rm -sf db          # destroy postgres container
  docker compose up -d db           # recreate it
  curl localhost:8080/notes         # 'first' is still there
  ```
```

- [ ] **Step 7: Smoke-run the solution**

```bash
cd 03-volumes/solution
docker compose up -d
sleep 5
curl -X POST localhost:8080/notes/first
curl localhost:8080/notes
docker compose down   # leave volume intact (no -v)
```
Expected: posting returns 201; GET returns the note as JSON.

- [ ] **Step 8: Commit**

```bash
git add 03-volumes
git commit -m "feat(03): volumes challenge + solution"
```

---

## Task 5: Challenge 04 — Networks

**Files:**
- Create: `04-networks/README.md`
- Create: `04-networks/starter/{app.py,requirements.txt}`
- Create: `04-networks/solution/{Dockerfile,app.py,requirements.txt,commands.md,NOTES.md}`

- [ ] **Step 1: Create `starter/app.py`**

```python
from flask import Flask
import os, redis

app = Flask(__name__)
r = redis.Redis(host=os.environ.get("REDIS_HOST", "redis"), port=6379, decode_responses=True)

@app.route("/")
def index():
    count = r.incr("hits")
    return f"<h1>Hit #{count}</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
```

- [ ] **Step 2: Create `starter/requirements.txt`**

```
flask==3.0.3
redis==5.0.8
```

- [ ] **Step 3: Create `README.md`**

```markdown
# Challenge 04 — Networks

## Goal
Get two containers talking by DNS name on a user-defined bridge network. Learn why the default bridge is a trap.

## Concepts introduced
- Default bridge network vs user-defined bridge.
- DNS resolution between containers (only on user-defined networks).
- Inspecting networks with `docker network inspect`.

## The challenge
Run two containers — the Flask app from `starter/` and a Redis instance — so that:

1. Both are on the **same user-defined bridge network**.
2. Flask reaches Redis by the **name** `redis`, not by IP address.
3. Stopping/disconnecting Redis breaks the app (proving the dependency is real).

Use raw `docker network` and `docker run` commands. Save them in `solution/commands.md`.

## Success criteria
- [ ] `docker network ls` shows your custom network.
- [ ] `curl localhost:8080` increments a counter (hit #1, #2, ...).
- [ ] `docker exec <flask> ping -c1 redis` resolves and replies.
- [ ] `docker network disconnect <net> <redis>` causes the next request to error.

## Hints
1. Create the network first: `docker network create lab-net`.
2. Then run each container with `--network lab-net --name <name>`.
3. The official Redis image is just `redis:7-alpine` — no extra config needed.

## Reference
- https://docs.docker.com/engine/network/drivers/bridge/
- https://docs.docker.com/engine/network/#dns-services
```

- [ ] **Step 4: Create `solution/Dockerfile`** (reuses Challenge 01 pattern)

```dockerfile
FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
EXPOSE 8080
CMD ["python", "app.py"]
```

- [ ] **Step 5: Copy starter app files into `solution/`**

```bash
cp 04-networks/starter/{app.py,requirements.txt} 04-networks/solution/
```

- [ ] **Step 6: Create `solution/commands.md`**

```markdown
# Solution — challenge 04 commands

```bash
# Build the Flask image
docker build -t ch04-web .

# Create a user-defined bridge network
docker network create lab-net

# Run Redis on the network (no port published — only Flask needs it)
docker run -d --name redis --network lab-net redis:7-alpine

# Run Flask on the same network; REDIS_HOST defaults to "redis" in the app
docker run -d --name web --network lab-net -p 8080:8080 ch04-web

# Test
curl localhost:8080   # Hit #1
curl localhost:8080   # Hit #2

# Prove DNS works
docker exec web ping -c1 redis

# Break the dependency
docker network disconnect lab-net redis
curl -i localhost:8080   # 500 (Redis unreachable)

# Cleanup
docker rm -f web redis
docker network rm lab-net
```
```

- [ ] **Step 7: Create `solution/NOTES.md`**

```markdown
# Notes — solution

- **Why a user-defined network:** on the default `bridge`, containers can reach each other only by IP, and IPs change. Docker only provides automatic DNS for **user-defined** bridge networks. Always create your own.
- **`--network` + `--name` = address book:** once a container is on a user-defined network, every other container on that network can reach it as `<container-name>`.
- **One process per container:** Redis is a separate container instead of being installed inside the Flask image. This is the Docker way: each service is independent, scalable, and replaceable.
- **Networks are first-class objects:** they outlive containers. Useful for keeping a dev stack wired together while you recreate one service.
```

- [ ] **Step 8: Smoke-run the solution**

```bash
cd 04-networks/solution
docker build -t ch04-web .
docker network create ch04-net
docker run -d --name ch04-redis --network ch04-net redis:7-alpine
docker run -d --name ch04-web --network ch04-net -p 8080:8080 ch04-web
sleep 2
curl -s localhost:8080
docker rm -f ch04-web ch04-redis
docker network rm ch04-net
```
Expected: `<h1>Hit #1</h1>` (or similar).

- [ ] **Step 9: Commit**

```bash
git add 04-networks
git commit -m "feat(04): networks challenge + solution"
```

---

## Task 6: Challenge 05 — Compose intro

**Files:**
- Create: `05-compose-intro/README.md`
- Create: `05-compose-intro/starter/{app.py,requirements.txt,Dockerfile}` (reuse Challenge 04 solution)
- Create: `05-compose-intro/solution/{compose.yaml,app.py,requirements.txt,Dockerfile,NOTES.md}`

- [ ] **Step 1: Copy Challenge 04 solution files into `starter/`**

```bash
cp 04-networks/solution/{app.py,requirements.txt,Dockerfile} 05-compose-intro/starter/
```

- [ ] **Step 2: Create `README.md`**

```markdown
# Challenge 05 — Compose intro

## Goal
Replace a manual chain of `docker network create` + `docker run` + `docker run` with a single `compose.yaml`. One file, one `up`, one `down`.

## Concepts introduced
- `compose.yaml` v2 structure: `services`, `build`, `image`, `ports`, `volumes`, `depends_on`.
- Default network: Compose creates one automatically and puts every service on it.
- Service names as DNS hostnames.
- `docker compose up`, `down`, `ps`, `logs`, `build`.

## The challenge
Take the working Flask+Redis setup from Challenge 04 and convert it into a single `compose.yaml`. Requirements:

1. Two services: `web` (built from the local `Dockerfile`) and `cache` (`redis:7-alpine`).
2. `web` reaches Redis at host `cache` (use the service name).
3. Host port 8080 is mapped to container port 8080 on `web`.
4. `docker compose up` brings everything online; `docker compose down` cleans up.

## Success criteria
- [ ] `docker compose up -d` (from inside `solution/`) succeeds.
- [ ] `curl localhost:8080` works and the counter increments.
- [ ] `docker compose ps` shows both services as running.
- [ ] `docker compose down` removes both containers and the auto-created network.

## Hints
1. The service name becomes the DNS hostname inside the auto-created network. So if you name the Redis service `cache`, set `REDIS_HOST=cache`.
2. `build: .` tells Compose to build the image from the Dockerfile in the current directory.
3. Compose v2 doesn't need a `version:` key at the top.

## Reference
- https://docs.docker.com/compose/intro/compose-application-model/
- https://docs.docker.com/reference/compose-file/services/
```

- [ ] **Step 3: Copy starter files into `solution/`**

```bash
cp 05-compose-intro/starter/{app.py,requirements.txt,Dockerfile} 05-compose-intro/solution/
```

- [ ] **Step 4: Create `solution/compose.yaml`**

```yaml
services:
  web:
    build: .
    ports:
      - "8080:8080"
    environment:
      REDIS_HOST: cache       # service name acts as DNS hostname
    depends_on:
      - cache

  cache:
    image: redis:7-alpine
```

- [ ] **Step 5: Create `solution/NOTES.md`**

```markdown
# Notes — solution

- **Compose creates a default network** named `<project>_default` and joins every service to it. No need to declare a `networks:` block for simple setups.
- **Service name = DNS name.** Inside the network, `cache` resolves to the Redis container's IP. That's why the app sets `REDIS_HOST=cache`.
- **`depends_on` only orders startup**, not readiness. Redis is fast so it doesn't matter here, but for Postgres we'll need `healthcheck` + `condition: service_healthy` (Challenge 06).
- **`docker compose down` removes containers AND the network.** Add `-v` to also remove named volumes (dangerous: deletes data).
```

- [ ] **Step 6: Smoke-run the solution**

```bash
cd 05-compose-intro/solution
docker compose up -d
sleep 2
curl -s localhost:8080
docker compose down
```
Expected: hit counter response.

- [ ] **Step 7: Commit**

```bash
git add 05-compose-intro
git commit -m "feat(05): compose intro challenge + solution"
```

---

## Task 7: Challenge 06 — Compose realistic

**Files:**
- Create: `06-compose-realistic/README.md`
- Create: `06-compose-realistic/starter/{app.py,requirements.txt,Dockerfile,initdb.d/01_schema.sql}`
- Create: `06-compose-realistic/solution/{compose.yaml,app.py,requirements.txt,Dockerfile,initdb.d/01_schema.sql,NOTES.md}`

- [ ] **Step 1: Create `starter/app.py`**

```python
from flask import Flask, jsonify
import os, time, psycopg, redis
from psycopg.rows import dict_row

app = Flask(__name__)

DSN = (
    f"host={os.environ['DB_HOST']} dbname={os.environ['DB_NAME']} "
    f"user={os.environ['DB_USER']} password={os.environ['DB_PASSWORD']}"
)
r = redis.Redis(host=os.environ.get("REDIS_HOST", "cache"), port=6379, decode_responses=True)

def wait_for_db(max_tries=30):
    for i in range(max_tries):
        try:
            with psycopg.connect(DSN) as conn:
                conn.execute("SELECT 1")
                return
        except Exception as e:
            print(f"[wait_for_db] attempt {i+1}: {e}", flush=True)
            time.sleep(1)
    raise RuntimeError("Database not reachable")

@app.route("/items")
def items():
    cached = r.get("items")
    if cached:
        return cached, 200, {"Content-Type": "application/json", "X-Cache": "HIT"}
    with psycopg.connect(DSN, row_factory=dict_row) as conn:
        rows = conn.execute("SELECT id, name FROM items ORDER BY id").fetchall()
    payload = jsonify(rows).get_data(as_text=True)
    r.setex("items", 30, payload)
    return payload, 200, {"Content-Type": "application/json", "X-Cache": "MISS"}

if __name__ == "__main__":
    wait_for_db()
    app.run(host="0.0.0.0", port=8080)
```

- [ ] **Step 2: Create `starter/requirements.txt`**

```
flask==3.0.3
psycopg[binary]==3.2.3
redis==5.0.8
```

- [ ] **Step 3: Create `starter/Dockerfile`**

```dockerfile
FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
EXPOSE 8080
CMD ["python", "app.py"]
```

- [ ] **Step 4: Create `starter/initdb.d/01_schema.sql`**

```sql
CREATE TABLE IF NOT EXISTS items (
    id   SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

INSERT INTO items (name) VALUES ('alpha'), ('beta'), ('gamma');
```

- [ ] **Step 5: Create `README.md`**

```markdown
# Challenge 06 — Compose realistic

## Goal
Stand up a realistic three-service stack — web + Postgres + Redis — where the web service waits for the database to be **actually ready** (not just started) before running.

## Concepts introduced
- `healthcheck` per service.
- `depends_on: condition: service_healthy`.
- Init scripts mounted into `/docker-entrypoint-initdb.d/` for Postgres bootstrap.
- `restart` policies in a compose context.

## The challenge
Inside `starter/` you have a Flask app that reads `items` from Postgres, caches them in Redis for 30s, and exposes `GET /items`. There's also a SQL bootstrap file in `starter/initdb.d/`.

Write a `compose.yaml` so that:

1. Three services: `web` (built from the local Dockerfile), `db` (`postgres:16-alpine`), `cache` (`redis:7-alpine`).
2. `db` has a healthcheck using `pg_isready`.
3. `web` uses `depends_on` with `condition: service_healthy` for `db` — it should **not** start before Postgres accepts connections.
4. `db` mounts the SQL files in `starter/initdb.d/` so the `items` table is created and seeded on first startup.
5. Postgres data persists across `docker compose down && up` via a named volume.
6. `restart: unless-stopped` on `web` so it survives intermittent failures.

## Success criteria
- [ ] `docker compose up -d` brings the stack online; `web` only becomes healthy after `db` is.
- [ ] `curl localhost:8080/items` returns `[{"id":1,"name":"alpha"},...]`.
- [ ] First call returns header `X-Cache: MISS`; subsequent calls within 30s return `X-Cache: HIT`.
- [ ] `docker compose down && docker compose up -d` preserves the items (volume survives).
- [ ] Stopping the DB while running the app produces a clean error in `web`'s logs without crashing it (restart policy keeps it alive).

## Hints
1. `healthcheck` for Postgres:
   ```yaml
   healthcheck:
     test: ["CMD-SHELL", "pg_isready -U $$POSTGRES_USER -d $$POSTGRES_DB"]
     interval: 2s
     timeout: 2s
     retries: 20
   ```
   The `$$` is required so Compose doesn't try to interpolate the variable itself.
2. To mount the init scripts: `./initdb.d:/docker-entrypoint-initdb.d:ro`.
3. The `wait_for_db()` in the app gives a second safety net — `condition: service_healthy` is the primary one.

## Reference
- https://docs.docker.com/reference/compose-file/services/#healthcheck
- https://docs.docker.com/reference/compose-file/services/#depends_on
- https://hub.docker.com/_/postgres (search for "initialization scripts")
```

- [ ] **Step 6: Copy starter files into `solution/`**

```bash
cp 06-compose-realistic/starter/{app.py,requirements.txt,Dockerfile} 06-compose-realistic/solution/
mkdir -p 06-compose-realistic/solution/initdb.d
cp 06-compose-realistic/starter/initdb.d/01_schema.sql 06-compose-realistic/solution/initdb.d/
```

- [ ] **Step 7: Create `solution/compose.yaml`**

```yaml
services:
  web:
    build: .
    ports:
      - "8080:8080"
    environment:
      DB_HOST: db
      DB_NAME: shop
      DB_USER: shop
      DB_PASSWORD: shop
      REDIS_HOST: cache
    depends_on:
      db:
        condition: service_healthy
      cache:
        condition: service_started
    restart: unless-stopped

  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: shop
      POSTGRES_USER: shop
      POSTGRES_PASSWORD: shop
    volumes:
      - pgdata:/var/lib/postgresql/data
      - ./initdb.d:/docker-entrypoint-initdb.d:ro   # runs on first init only
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U $$POSTGRES_USER -d $$POSTGRES_DB"]
      interval: 2s
      timeout: 2s
      retries: 20

  cache:
    image: redis:7-alpine

volumes:
  pgdata:
```

- [ ] **Step 8: Create `solution/NOTES.md`**

```markdown
# Notes — solution

- **`depends_on` without `condition`** only orders startup, not readiness. With `condition: service_healthy` Compose waits until the dependency's healthcheck returns success.
- **`/docker-entrypoint-initdb.d/`** is run by the Postgres image only on first initialisation of the data directory. Once `pgdata` has files in it, the scripts are skipped — so editing them after the first up won't re-seed.
- **`$$POSTGRES_USER`** in the healthcheck command: a single `$` would make Compose interpolate the value before passing it to the container. `$$` escapes that so the variable is resolved by the shell inside the container, where it's actually set.
- **Restart policy** matters here because the app intentionally crashes if it can't reach Postgres on startup. `unless-stopped` brings it back automatically once the dependency recovers.
```

- [ ] **Step 9: Smoke-run the solution**

```bash
cd 06-compose-realistic/solution
docker compose up -d
sleep 10
curl -s -i localhost:8080/items | head -20
curl -s -i localhost:8080/items | head -20    # second call should be HIT
docker compose down                            # leave volume
```
Expected: items returned; X-Cache transitions from MISS to HIT.

- [ ] **Step 10: Commit**

```bash
git add 06-compose-realistic
git commit -m "feat(06): realistic compose challenge + solution"
```

---

## Task 8: Challenge 07 — Dev workflow

**Files:**
- Create: `07-dev-workflow/README.md`
- Create: `07-dev-workflow/starter/{app.py,requirements.txt,Dockerfile,compose.yaml}` (production-style baseline from Ch06, simplified)
- Create: `07-dev-workflow/solution/{Dockerfile,compose.yaml,compose.override.yaml,app.py,requirements.txt,NOTES.md}`

- [ ] **Step 1: Create `starter/app.py`**

```python
from flask import Flask
import os, sys

app = Flask(__name__)

@app.route("/")
def hello():
    return f"<h1>Hello from {os.environ.get('STAGE', 'prod')}</h1>"

if __name__ == "__main__":
    # Production server stub (no reload).
    app.run(host="0.0.0.0", port=8080, debug=False)
```

- [ ] **Step 2: Create `starter/requirements.txt`**

```
flask==3.0.3
debugpy==1.8.5
```

- [ ] **Step 3: Create `starter/Dockerfile`**

```dockerfile
FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
EXPOSE 8080
CMD ["python", "app.py"]
```

- [ ] **Step 4: Create `starter/compose.yaml`** (production-like baseline)

```yaml
services:
  web:
    build: .
    ports:
      - "8080:8080"
    environment:
      STAGE: prod
```

- [ ] **Step 5: Create `README.md`**

```markdown
# Challenge 07 — Dev workflow

## Goal
Run the same app in two flavours from the same `compose.yaml`: a clean production-like build for verification, and a dev experience with hot reload + a debugger attached — without touching the prod file.

## Concepts introduced
- `compose.override.yaml` (loaded automatically by `docker compose up`).
- Bind-mounting source into the container for live editing.
- Flask `debug=True` for auto-reload (and `debugpy` exposed on a port for VS Code).
- Reading logs of a single service.

## The challenge
You start with a working `compose.yaml` that runs the app in prod-like mode. Add a `compose.override.yaml` (do NOT modify the prod file) so that the default `docker compose up` provides:

1. Bind mount of the host source into `/app` so edits show up live.
2. Hot reload (Flask debug mode, or `--reload`).
3. Debugger port `5678` exposed for VS Code / `debugpy` attach.
4. `STAGE=dev` overrides the prod value.

You must keep the original `compose.yaml` usable as-is for "prod" verification:
- `docker compose -f compose.yaml up` (override skipped) → prod behaviour.
- `docker compose up` (default loads override) → dev behaviour.

## Success criteria
- [ ] `docker compose -f compose.yaml up -d` runs prod mode — editing `app.py` does NOT update the response without a rebuild.
- [ ] `docker compose up -d` runs dev mode — editing `app.py` updates the response after Flask reloads.
- [ ] `docker compose up -d` exposes port 5678 to the host.
- [ ] `curl localhost:8080` returns "Hello from dev" in dev mode and "Hello from prod" in prod mode.

## Hints
1. `compose.override.yaml` is merged on top of `compose.yaml` automatically. Override keys win; arrays may be concatenated or replaced depending on the key (consult the docs for `command:` vs `volumes:`).
2. To force-reload, replace the prod `CMD` by overriding `command:` in the override file. Run with something like:
   `python -m debugpy --listen 0.0.0.0:5678 -m flask --app app run --host 0.0.0.0 --port 8080 --reload`.
3. The override file does **not** need its own `image:` or `build:` — it inherits from the base.

## Reference
- https://docs.docker.com/compose/how-tos/multiple-compose-files/merge/
- https://flask.palletsprojects.com/en/stable/cli/#run-the-development-server
```

- [ ] **Step 6: Copy starter files into `solution/`**

```bash
cp 07-dev-workflow/starter/{app.py,requirements.txt,Dockerfile,compose.yaml} 07-dev-workflow/solution/
```

- [ ] **Step 7: Create `solution/compose.override.yaml`**

```yaml
services:
  web:
    environment:
      STAGE: dev
    volumes:
      - ./:/app                               # live source
    ports:
      - "5678:5678"                           # debugpy
    command: >
      python -m debugpy --listen 0.0.0.0:5678
      -m flask --app app run --host 0.0.0.0 --port 8080 --reload
```

- [ ] **Step 8: Create `solution/NOTES.md`**

```markdown
# Notes — solution

- **Compose auto-merges** `compose.yaml` + `compose.override.yaml` when you run `docker compose up`. To opt out, pass `-f compose.yaml` explicitly.
- **Why bind-mount the whole directory** instead of just `app.py`: any new files you create on the host (e.g. a `models.py`) are picked up too.
- **Hot reload caveats:** Flask's `--reload` watches Python files. New imports may need a manual restart. Editing `requirements.txt` always needs a rebuild.
- **Attaching VS Code:** add a `.vscode/launch.json` with `"type": "debugpy", "request": "attach", "connect": {"host": "localhost", "port": 5678}` — but that's outside Docker's scope.
- **Two-file pattern scales:** a `compose.test.yaml` selected with `-f compose.yaml -f compose.test.yaml` can swap in test databases, etc.
```

- [ ] **Step 9: Smoke-run the solution (dev mode)**

```bash
cd 07-dev-workflow/solution
docker compose up -d
sleep 3
curl -s localhost:8080      # expect "Hello from dev"
docker compose down
```

- [ ] **Step 10: Commit**

```bash
git add 07-dev-workflow
git commit -m "feat(07): dev workflow with override.yaml challenge + solution"
```

---

## Task 9: Challenge 08 — Multi-stage builds

**Files:**
- Create: `08-multi-stage/README.md`
- Create: `08-multi-stage/starter/{app.py,requirements.txt}`
- Create: `08-multi-stage/solution/{Dockerfile,app.py,requirements.txt,NOTES.md}`

- [ ] **Step 1: Create `starter/app.py`**

```python
from flask import Flask
from cryptography.fernet import Fernet

app = Flask(__name__)
KEY = Fernet.generate_key()
F = Fernet(KEY)

@app.route("/")
def index():
    token = F.encrypt(b"secret payload")
    return {"token": token.decode(), "key": KEY.decode()}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
```

- [ ] **Step 2: Create `starter/requirements.txt`**

```
flask==3.0.3
cryptography==43.0.1
```

(`cryptography` pulls in `cffi` and triggers a real C build on slim images.)

- [ ] **Step 3: Create `README.md`**

```markdown
# Challenge 08 — Multi-stage builds

## Goal
Build a final image that contains your app and its runtime deps, but **none** of the C compilers or build tools used during installation.

## Concepts introduced
- `FROM ... AS builder` — naming a build stage.
- `COPY --from=builder` — pulling artefacts from a previous stage.
- Wheels (`pip wheel`) as the transfer format between stages.
- Why "slim" or "distroless" runtime bases shrink images and attack surface.

## The challenge
The app uses `cryptography`, which compiles native code if no prebuilt wheel matches the platform. A naïve single-stage Dockerfile with `python:3.13-slim` either fails to build (no `gcc`) or works after you `apt-get install build-essential` — leaving ~250 MB of build tools in the final image.

Write a multi-stage Dockerfile that:

1. Uses a build stage with the toolchain to compile / install dependencies.
2. Uses a clean runtime stage (`python:3.13-slim`) that does NOT install any build tools.
3. Copies installed packages from the build stage into the runtime stage.
4. Produces a final image whose `which gcc` returns nothing and whose size is under 100 MB.

## Success criteria
- [ ] `docker build -t ch08 .` succeeds without `apt-get install build-essential` in the final stage.
- [ ] `docker run --rm -p 8080:8080 ch08` serves a token at `/`.
- [ ] `docker run --rm ch08 sh -c "which gcc; which cc; which make"` prints nothing.
- [ ] `docker image inspect ch08 --format '{{.Size}}'` returns a value under 100 MB (100_000_000 bytes).

## Hints
1. Build stage: install `build-essential` and `libffi-dev`, then `pip install --prefix=/install -r requirements.txt`.
2. Runtime stage: `COPY --from=builder /install /usr/local` to drop the packages into the standard Python path.
3. No need to copy `/usr/bin/gcc` etc. — they stay in the builder, which is discarded.

## Reference
- https://docs.docker.com/build/building/multi-stage/
- https://pythonspeed.com/articles/multi-stage-docker-python/
```

- [ ] **Step 4: Copy starter app files into `solution/`**

```bash
cp 08-multi-stage/starter/{app.py,requirements.txt} 08-multi-stage/solution/
```

- [ ] **Step 5: Create `solution/Dockerfile`**

```dockerfile
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
```

- [ ] **Step 6: Create `solution/NOTES.md`**

```markdown
# Notes — solution

- **Why two stages:** `gcc`, headers and `apt` caches are needed to install, but NEVER at runtime. A second `FROM` resets to a clean image and we drop only the artefacts.
- **`pip install --prefix=/install`** puts the packages under `/install/lib/python3.13/site-packages` etc. Copying `/install` into `/usr/local` of the runtime stage places them where Python looks by default.
- **Alternative: wheels.** Run `pip wheel -w /wheels -r requirements.txt` in the builder, then `pip install --no-index --find-links=/wheels -r requirements.txt` in the runtime. More portable but two pip runs.
- **`--target=foo` in newer pip versions** is another option, but `--prefix` plays best with `python -m site` paths.
- **Smaller still?** `python:3.13-slim` → distroless (`gcr.io/distroless/python3-debian12`). No shell, no apt — debugging is harder, so save it for prod-grade images.
```

- [ ] **Step 7: Smoke-build the solution**

```bash
cd 08-multi-stage/solution
docker build -t ch08 .
docker run --rm ch08 sh -c "which gcc || echo no-gcc"
docker image inspect ch08 --format '{{.Size}}'
```
Expected: build succeeds; `no-gcc` printed; size under 100_000_000 bytes.

- [ ] **Step 8: Commit**

```bash
git add 08-multi-stage
git commit -m "feat(08): multi-stage build challenge + solution"
```

---

## Task 10: Challenge 09 — Env and secrets (dev-grade)

**Files:**
- Create: `09-env-and-secrets/README.md`
- Create: `09-env-and-secrets/starter/{app.py,requirements.txt,Dockerfile,compose.yaml}` (simplified from Ch06)
- Create: `09-env-and-secrets/solution/{compose.yaml,.env.example,.gitignore,app.py,requirements.txt,Dockerfile,NOTES.md}`

- [ ] **Step 1: Create `starter/app.py`**

```python
from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
    debug = os.environ.get("APP_DEBUG", "false")
    db_user = os.environ.get("DB_USER", "?")
    # Intentionally do NOT print DB_PASSWORD — secret hygiene.
    return {"debug": debug, "db_user": db_user}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("APP_PORT", "8080")))
```

- [ ] **Step 2: Create `starter/requirements.txt`**

```
flask==3.0.3
```

- [ ] **Step 3: Create `starter/Dockerfile`**

```dockerfile
FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
EXPOSE 8080
CMD ["python", "app.py"]
```

- [ ] **Step 4: Create `starter/compose.yaml`** (hard-coded, what the learner will fix)

```yaml
services:
  web:
    build: .
    ports:
      - "8080:8080"
    environment:
      APP_DEBUG: "true"
      APP_PORT: "8080"
      DB_USER: shop
      DB_PASSWORD: HARDCODED_BAD_PASSWORD
```

- [ ] **Step 5: Create `README.md`**

```markdown
# Challenge 09 — Env and secrets (dev-grade)

## Goal
Stop hard-coding configuration in `compose.yaml`. Use a `.env` file for values that change per environment, document them in a checked-in `.env.example`, and keep real secrets out of git.

## Concepts introduced
- `ENV` (in Dockerfile) vs `environment:` (in compose) vs `env_file:` (in compose).
- The implicit `.env` file picked up by `docker compose` for variable interpolation.
- `.env.example` as documentation that ships with the repo.
- Why baking secrets into images is a one-way trip (anyone with the image has the secret).

## The challenge
`starter/compose.yaml` has a hard-coded password and tightly-coupled values. Refactor so that:

1. All tunable values (`APP_PORT`, `APP_DEBUG`, `DB_USER`, `DB_PASSWORD`) live in a `.env` file at the project root.
2. `compose.yaml` references them with `${VAR}` interpolation OR uses `env_file:` to pass them into the container.
3. A `.env.example` documents every variable with safe sample values and inline comments.
4. A `.gitignore` ensures the real `.env` is never committed.
5. The image itself (built without the runtime env) contains no secret — `docker inspect <image>` reveals no password.

## Success criteria
- [ ] Running `cp .env.example .env` and `docker compose up -d` works end-to-end.
- [ ] `curl localhost:${APP_PORT}` returns the JSON with the configured user (no password).
- [ ] `docker image inspect $(docker compose images -q web)` shows no secret in `Env` or `Labels`.
- [ ] `git check-ignore .env` prints `.env` (i.e. it would be skipped by git).
- [ ] Changing `APP_PORT` in `.env` and restarting maps the new port without touching `compose.yaml`.

## Hints
1. Compose auto-loads a `.env` file next to `compose.yaml` for `${VAR}` interpolation. Different from `env_file:`, which forwards a file into the container.
2. Use both:
   - `${APP_PORT}` interpolation for things Compose itself needs (ports).
   - `env_file: .env` for things the container needs at runtime (DB creds).
3. `.env.example` should be committed; `.env` should NOT.

## Reference
- https://docs.docker.com/compose/how-tos/environment-variables/set-environment-variables/
- https://docs.docker.com/compose/how-tos/environment-variables/variable-interpolation/
```

- [ ] **Step 6: Copy starter app files into `solution/`**

```bash
cp 09-env-and-secrets/starter/{app.py,requirements.txt,Dockerfile} 09-env-and-secrets/solution/
```

- [ ] **Step 7: Create `solution/compose.yaml`**

```yaml
services:
  web:
    build: .
    ports:
      - "${APP_PORT}:${APP_PORT}"     # Compose interpolates from .env
    env_file:
      - .env                          # forwarded into the container
    environment:
      APP_PORT: "${APP_PORT}"         # also pin APP_PORT explicitly for the app
```

- [ ] **Step 8: Create `solution/.env.example`**

```dotenv
# App
APP_PORT=8080
APP_DEBUG=false

# Database (used by the app at runtime — NOT baked into the image)
DB_USER=shop
DB_PASSWORD=changeme        # set a real value in your local .env
```

- [ ] **Step 9: Create `solution/.gitignore`**

```
.env
```

- [ ] **Step 10: Create `solution/NOTES.md`**

```markdown
# Notes — solution

- **Three layers of env variables in compose:**
  1. The `.env` file next to `compose.yaml` — Compose reads it ONLY for `${VAR}` interpolation in the YAML itself.
  2. `environment:` block — sets vars in the container; values can come from the host or `${VAR}`.
  3. `env_file:` — Compose reads each line and forwards it to the container at runtime, no interpolation in the YAML.
- **Never put secrets in `ENV` inside a Dockerfile.** They become part of the image's history; anyone who pulls the image gets them.
- **`.env` is dev-grade.** For prod, use a secret manager (Vault, AWS Secrets Manager, K8s Secrets) and inject at runtime. Out of scope for this roadmap but worth knowing.
- **Pattern for new repos:** commit `.env.example`, gitignore `.env`, document the variables in the README's "Getting started" section.
```

- [ ] **Step 11: Smoke-run the solution**

```bash
cd 09-env-and-secrets/solution
cp .env.example .env
docker compose up -d
sleep 2
curl -s localhost:8080
docker compose down
```
Expected: JSON with `db_user: shop` and `debug: false`.

- [ ] **Step 12: Commit**

```bash
git add 09-env-and-secrets
git commit -m "feat(09): env and secrets challenge + solution"
```

---

## Task 11: Challenge 10 — Final challenge

**Files:**
- Create: `10-final-challenge/README.md`
- Create: `10-final-challenge/starter/{api/,worker/,proxy/}` (skeletons only — no Dockerfiles, no compose)
- Create: `10-final-challenge/solution/{compose.yaml,compose.override.yaml,.env.example,.gitignore,api/,worker/,db/initdb.d/,proxy/,NOTES.md}`

This task is bigger; split into substeps.

### 11.A Starter — `api/`

- [ ] **Step 1: Create `starter/api/app.py`**

```python
from flask import Flask, request, jsonify
import os, psycopg, redis, json, uuid

app = Flask(__name__)

DSN = (
    f"host={os.environ['DB_HOST']} dbname={os.environ['DB_NAME']} "
    f"user={os.environ['DB_USER']} password={os.environ['DB_PASSWORD']}"
)
r = redis.Redis(host=os.environ["REDIS_HOST"], port=6379, decode_responses=True)

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/jobs", methods=["POST"])
def submit():
    payload = request.get_json() or {}
    job_id = str(uuid.uuid4())
    with psycopg.connect(DSN) as conn:
        conn.execute(
            "INSERT INTO jobs (id, payload, status) VALUES (%s, %s, 'pending')",
            (job_id, json.dumps(payload)),
        )
        conn.commit()
    r.lpush("jobs", job_id)
    return {"id": job_id}, 201

@app.route("/jobs/<job_id>")
def status(job_id):
    with psycopg.connect(DSN) as conn:
        row = conn.execute(
            "SELECT id, status, result FROM jobs WHERE id = %s", (job_id,)
        ).fetchone()
    if not row:
        return {"error": "not found"}, 404
    return {"id": row[0], "status": row[1], "result": row[2]}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("APP_PORT", "8080")))
```

- [ ] **Step 2: Create `starter/api/requirements.txt`**

```
flask==3.0.3
psycopg[binary]==3.2.3
redis==5.0.8
```

### 11.B Starter — `worker/`

- [ ] **Step 3: Create `starter/worker/worker.py`**

```python
import os, time, json, psycopg, redis

DSN = (
    f"host={os.environ['DB_HOST']} dbname={os.environ['DB_NAME']} "
    f"user={os.environ['DB_USER']} password={os.environ['DB_PASSWORD']}"
)
r = redis.Redis(host=os.environ["REDIS_HOST"], port=6379, decode_responses=True)

def process(payload: dict) -> str:
    # Toy processing: uppercase a 'message' if present.
    return (payload.get("message") or "").upper()

def main():
    print("[worker] listening on jobs queue", flush=True)
    while True:
        item = r.brpop("jobs", timeout=5)
        if not item:
            continue
        _, job_id = item
        with psycopg.connect(DSN) as conn:
            row = conn.execute("SELECT payload FROM jobs WHERE id = %s", (job_id,)).fetchone()
            if not row:
                continue
            payload = json.loads(row[0])
            result = process(payload)
            conn.execute(
                "UPDATE jobs SET status='done', result=%s WHERE id=%s",
                (result, job_id),
            )
            conn.commit()
        print(f"[worker] processed {job_id} → {result}", flush=True)

if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Create `starter/worker/requirements.txt`**

```
psycopg[binary]==3.2.3
redis==5.0.8
```

### 11.C Starter — `proxy/`

- [ ] **Step 5: Create `starter/proxy/nginx.conf`**

```nginx
events {}
http {
    upstream api { server api:8080; }
    server {
        listen 80;
        location / {
            proxy_pass http://api;
            proxy_set_header Host $host;
        }
    }
}
```

### 11.D README

- [ ] **Step 6: Create `README.md`**

```markdown
# Challenge 10 — Final challenge: API + worker + DB + cache + proxy

## Goal
Wire everything you've learned into one realistic stack: a REST API enqueues jobs into Redis, a worker processes them and writes results to Postgres, Nginx fronts the API, and the whole thing has a clean dev workflow on top of a prod-like baseline.

## Concepts revisited
- Multi-stage Dockerfiles for the Python services.
- User-defined network (auto, via Compose).
- Named volume for Postgres data.
- Healthchecks and `depends_on: condition: service_healthy`.
- `.env` configuration + `.gitignore`.
- `compose.override.yaml` for the dev experience.

## The challenge
`starter/` ships application code only — no Dockerfiles, no compose, no init scripts. Build:

1. `api/Dockerfile` — multi-stage, slim final image.
2. `worker/Dockerfile` — multi-stage, slim final image.
3. `db/initdb.d/01_schema.sql` — creates a `jobs(id, payload, status, result)` table.
4. `compose.yaml` — five services: `api`, `worker`, `db`, `cache`, `proxy`. Postgres has a healthcheck; `api` and `worker` wait for it. Named volume for `pgdata`. Nginx forwards from host port 80 to `api:8080`.
5. `compose.override.yaml` — bind-mount source for `api` and `worker`; enable Flask reload on `api`.
6. `.env.example` + `.gitignore` for configuration.

## Success criteria
- [ ] `cp .env.example .env && docker compose up -d` brings the whole stack online.
- [ ] `curl localhost/health` returns `{"status":"ok"}` (via Nginx).
- [ ] `curl -X POST localhost/jobs -H 'Content-Type: application/json' -d '{"message":"hi"}'` returns a job id.
- [ ] Within 5 seconds, `curl localhost/jobs/<id>` returns `{"status":"done","result":"HI",...}`.
- [ ] `docker compose down && docker compose up -d` preserves jobs in the database.
- [ ] No `gcc` in the final api/worker images: `docker run --rm <image> which gcc` is empty.

## Hints
1. Reuse the multi-stage Dockerfile from Challenge 08 for both `api` and `worker`. Worker doesn't need `EXPOSE`.
2. Postgres healthcheck: same `pg_isready` recipe as Challenge 06.
3. Nginx config is already provided in `starter/proxy/nginx.conf`. Just mount it.
4. The override file can override `command:` for `api` to use `flask run --reload` (mirroring Challenge 07).
5. `.env` should hold: `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `APP_PORT`.

## Reference
- All previous challenges' READMEs.
- https://docs.docker.com/compose/how-tos/multiple-compose-files/merge/
```

### 11.E Solution

- [ ] **Step 7: Copy starter content into `solution/` skeleton**

```bash
mkdir -p 10-final-challenge/solution/{api,worker,proxy,db/initdb.d}
cp 10-final-challenge/starter/api/{app.py,requirements.txt}        10-final-challenge/solution/api/
cp 10-final-challenge/starter/worker/{worker.py,requirements.txt}  10-final-challenge/solution/worker/
cp 10-final-challenge/starter/proxy/nginx.conf                     10-final-challenge/solution/proxy/
```

- [ ] **Step 8: Create `solution/api/Dockerfile`** (multi-stage)

```dockerfile
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
```

- [ ] **Step 9: Create `solution/worker/Dockerfile`** (multi-stage)

```dockerfile
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
COPY worker.py .
CMD ["python", "worker.py"]
```

- [ ] **Step 10: Create `solution/db/initdb.d/01_schema.sql`**

```sql
CREATE TABLE IF NOT EXISTS jobs (
    id      TEXT PRIMARY KEY,
    payload JSONB NOT NULL,
    status  TEXT NOT NULL DEFAULT 'pending',
    result  TEXT
);
```

- [ ] **Step 11: Create `solution/compose.yaml`**

```yaml
services:
  proxy:
    image: nginx:1.27-alpine
    ports:
      - "80:80"
    volumes:
      - ./proxy/nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on:
      - api

  api:
    build: ./api
    environment:
      DB_HOST: db
      DB_NAME: ${POSTGRES_DB}
      DB_USER: ${POSTGRES_USER}
      DB_PASSWORD: ${POSTGRES_PASSWORD}
      REDIS_HOST: cache
      APP_PORT: "8080"
    depends_on:
      db:
        condition: service_healthy
      cache:
        condition: service_started
    restart: unless-stopped

  worker:
    build: ./worker
    environment:
      DB_HOST: db
      DB_NAME: ${POSTGRES_DB}
      DB_USER: ${POSTGRES_USER}
      DB_PASSWORD: ${POSTGRES_PASSWORD}
      REDIS_HOST: cache
    depends_on:
      db:
        condition: service_healthy
      cache:
        condition: service_started
    restart: unless-stopped

  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: ${POSTGRES_DB}
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    volumes:
      - pgdata:/var/lib/postgresql/data
      - ./db/initdb.d:/docker-entrypoint-initdb.d:ro
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U $$POSTGRES_USER -d $$POSTGRES_DB"]
      interval: 2s
      timeout: 2s
      retries: 20

  cache:
    image: redis:7-alpine

volumes:
  pgdata:
```

- [ ] **Step 12: Create `solution/compose.override.yaml`**

```yaml
services:
  api:
    volumes:
      - ./api:/app
    command: >
      python -m flask --app app run --host 0.0.0.0 --port 8080 --reload

  worker:
    volumes:
      - ./worker:/app
    # Worker has no reload; just rerun on file change manually.
```

- [ ] **Step 13: Create `solution/.env.example`**

```dotenv
POSTGRES_DB=jobs
POSTGRES_USER=jobs
POSTGRES_PASSWORD=changeme
APP_PORT=8080
```

- [ ] **Step 14: Create `solution/.gitignore`**

```
.env
```

- [ ] **Step 15: Create `solution/NOTES.md`**

```markdown
# Notes — solution

- **Service responsibilities are crisp:** `api` accepts HTTP and enqueues. `worker` only reads the queue and writes results. They share `db` and `cache` but never call each other directly.
- **Nginx is dumb on purpose.** Its only job is to forward port 80 → `api:8080`. Adds TLS termination, rate limiting, or load balancing later if you want — but starting simple makes failures obvious.
- **`depends_on: service_healthy` on Postgres** stops the api/worker from racing against an uninitialised DB. Without it you'd see flaky startup failures on cold boots.
- **Why multi-stage for both:** `psycopg[binary]` ships wheels, but `libpq` headers (`libpq-dev`) are still needed for some platforms — keeping them out of the runtime image saves space and surface.
- **Dev workflow:** the override mounts source for both services so you can iterate without rebuilds. The worker doesn't auto-reload — just `docker compose restart worker` after edits.
- **Production deltas (out of scope):** real secret manager instead of `.env`; image tags pinned by digest; resource limits; centralised logs; TLS at the proxy; replicated workers.
```

- [ ] **Step 16: Smoke-run the solution**

```bash
cd 10-final-challenge/solution
cp .env.example .env
docker compose up -d --build
sleep 15
curl -s localhost/health
JOB=$(curl -s -X POST localhost/jobs -H 'Content-Type: application/json' -d '{"message":"hi"}' | python3 -c "import json,sys; print(json.load(sys.stdin)['id'])")
sleep 5
curl -s localhost/jobs/$JOB
docker compose down
```
Expected: `{"status":"ok"}`, a job id, then a result `"HI"` and status `"done"`.

- [ ] **Step 17: Commit**

```bash
git add 10-final-challenge
git commit -m "feat(10): final multi-service challenge + solution"
```

---

## Task 12: Smoke-test sweep across all solutions

**Goal:** Catch any solution that doesn't actually run. Each solution was smoke-tested at the end of its own task, but environments drift — re-run them in sequence to confirm the full set still works.

- [ ] **Step 1: Clean any leftover state**

```bash
docker system prune -af --volumes
```

WARNING: this removes ALL unused images, containers, volumes on the machine. Confirm with the user before running if they have unrelated Docker work in progress.

- [ ] **Step 2: Run each solution in order**

For challenges with a `solution/compose.yaml`:
```bash
for d in 03-volumes 05-compose-intro 06-compose-realistic 07-dev-workflow 09-env-and-secrets 10-final-challenge; do
  echo "=== $d ==="
  cd "$d/solution"
  [ -f .env.example ] && cp .env.example .env
  docker compose up -d --build
  sleep 10
  docker compose ps
  docker compose down -v
  cd -
done
```

For Dockerfile-only solutions (01, 02, 04, 08):
```bash
for d in 01-dockerfile-basics 02-run-deep-dive 04-networks 08-multi-stage; do
  echo "=== $d ==="
  cd "$d/solution"
  docker build -t "smoke-${d}" .
  cd -
done
```

- [ ] **Step 3: Document any failures**

If a solution fails to start, fix the underlying file (treat it as a bug) and commit the fix with a `fix(NN): ...` message. Do NOT mark the plan complete until every solution runs.

- [ ] **Step 4: Clean up smoke-test images**

```bash
docker image rm smoke-01-dockerfile-basics smoke-02-run-deep-dive smoke-04-networks smoke-08-multi-stage 2>/dev/null || true
```

- [ ] **Step 5: Commit (only if fixes were needed)**

```bash
git add -A
git commit -m "fix: smoke-test sweep adjustments" || echo "nothing to commit"
```

---

## Task 13: Open the pull request

- [ ] **Step 1: Push the branch**

```bash
git push -u origin feature/docker-learning-roadmap
```

- [ ] **Step 2: Open the PR**

```bash
gh pr create --title "feat: hands-on Docker learning roadmap (10 challenges)" --body "$(cat <<'EOF'
## Summary
- Adds a 10-challenge, hands-on Docker learning roadmap at the repo root.
- Each folder ships a problem statement (`README.md`), starter files, and a runnable reference solution.
- Tops it with a new root `README.md` (index) and a curated `RESOURCES.md`.
- Spec: `docs/superpowers/specs/2026-05-15-docker-learning-roadmap-design.md`
- Plan: `docs/superpowers/plans/2026-05-15-docker-learning-roadmap.md`

## Test plan
- [ ] Run `docker compose up -d` inside each `solution/` that has a `compose.yaml` and verify success criteria.
- [ ] Run `docker build .` inside each Dockerfile-only `solution/` and verify it builds clean.
- [ ] Read each `README.md` from a learner's POV — are hints progressive, are success criteria verifiable?

🤖 Generated with [Claude Code](https://claude.com/claude-code)
EOF
)"
```

- [ ] **Step 3: Share the PR URL with the user**

Print the URL returned by `gh pr create`. Do NOT auto-merge; the user reviews.

---

## Self-review (already done by author)

- **Spec coverage:** every spec section has at least one task. Out-of-scope items (registries, K8s, CI/CD, prod observability) intentionally absent.
- **Placeholder scan:** no TBD / TODO / "fill in" markers in any task. All Dockerfiles, compose files, and READMEs are fully written.
- **Type / identifier consistency:** service names are stable across challenges that reuse them (`web`, `db`, `cache`, `api`, `worker`, `proxy`). Env var names consistent (`DB_HOST`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `REDIS_HOST`, `APP_PORT`). Challenge numbering matches spec.
