# Office Joke Laugh-Off entry: one deterministic one-liner, written to /output/entry.txt.
# Standard library only, no network. The bytes are identical on every run.
import os

JOKE = "My boss said we're a family, so I asked HR who gets custody of my weekends."

OUTPUT_PATH = "/output/entry.txt"

os.makedirs("/output", exist_ok=True)
with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
    handle.write(JOKE)
