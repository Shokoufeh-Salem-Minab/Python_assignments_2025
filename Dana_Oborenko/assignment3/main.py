# to run programm 
# pip3 install -r Dana_Oborenko/assignment3/requirements.txt
# python3 Dana_Oborenko/assignment3/main.py


from __future__ import annotations

from pathlib import Path  # built-in library
from datetime import datetime  # built-in library
import requests  # external library

from utils import read_lines, write_json  


def main() -> None:
    project_dir = Path(__file__).parent
    input_file = project_dir / "data" / "input.txt"
    output_file = project_dir / "output" / "results.json"

    # File operation: read
    words = read_lines(input_file)

    # External library: HTTP request to a public API
    joke = None
    try:
        resp = requests.get(
            "https://official-joke-api.appspot.com/random_joke",
            timeout=10
        )
        resp.raise_for_status()
        payload = resp.json()
        joke = f"{payload.get('setup', '')} — {payload.get('punchline', '')}".strip(" —")
    except Exception as e:
        joke = f"Could not fetch a joke. Error: {e}"

    result = {
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "words_count": len(words),
        "words_uppercase": [w.upper() for w in words],
        "joke_from_api": joke,
    }

    # File operation: write
    write_json(output_file, result)

    print("Done! Results saved to:", output_file)


if __name__ == "__main__":
    main()
