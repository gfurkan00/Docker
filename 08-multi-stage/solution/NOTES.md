# Notes — solution

- **Why two stages:** `gcc`, headers and `apt` caches are needed to install, but NEVER at runtime. A second `FROM` resets to a clean image and we drop only the artefacts.
- **`pip install --prefix=/install`** puts the packages under `/install/lib/python3.13/site-packages` etc. Copying `/install` into `/usr/local` of the runtime stage places them where Python looks by default.
- **Alternative: wheels.** Run `pip wheel -w /wheels -r requirements.txt` in the builder, then `pip install --no-index --find-links=/wheels -r requirements.txt` in the runtime. More portable but two pip runs.
- **`--target=foo` in newer pip versions** is another option, but `--prefix` plays best with `python -m site` paths.
- **Smaller still?** `python:3.13-slim` → distroless (`gcr.io/distroless/python3-debian12`). No shell, no apt — debugging is harder, so save it for prod-grade images.
