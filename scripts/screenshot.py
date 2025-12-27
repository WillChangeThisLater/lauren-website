#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "playwright",
# ]
# ///
import argparse
import math
import subprocess
import sys
import tempfile
from pathlib import Path
from urllib.parse import urlparse

from playwright.sync_api import sync_playwright


VIEWPORT = {"width": 1280, "height": 900}

def ensure_chromium() -> None:
    try:
        subprocess.run(
            [sys.executable, "-m", "playwright", "install", "chromium"],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError:
        raise RuntimeError(
            "Playwright could not download Chromium. Please run 'playwright install chromium' manually."
        )

def _normalize_argument(argument: str) -> str:
    if argument.startswith("siteshot-frames:"):
        argument = argument.split(":", 1)[1]
    argument = argument.strip()
    if not argument:
        raise ValueError("No URL provided to siteshot")

    parsed = urlparse(argument)
    if not parsed.scheme:
        argument = f"https://{argument}"
    return argument

def capture_screenshots(url: str, out_dir: Path, viewport_height: int = 900) -> list[Path]:
    ensure_chromium()

    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page(viewport=VIEWPORT)
        page.goto(url)
        page.wait_for_timeout(2000)

        scroll_height = page.evaluate("() => document.body.scrollHeight")
        if not scroll_height:
            scroll_height = viewport_height

        step = viewport_height
        num_screenshots = math.ceil(scroll_height / step)

        captured = []
        for index in range(num_screenshots):
            scroll_y = index * step
            page.evaluate("(y) => window.scrollTo(0, y)", scroll_y)
            page.wait_for_timeout(1000)
            output_path = out_dir / f"{index}.jpg"  # Updated file naming
            page.screenshot(path=str(output_path))
            captured.append(output_path)

        browser.close()

    return captured

def main():
    parser = argparse.ArgumentParser(description="Capture tiled screenshots of a webpage.")
    parser.add_argument("url", help="The URL to capture screenshots from.")
    parser.add_argument("--dir", type=str, help="Optional directory to save screenshots. If not specified, a temporary directory will be used.")
    args = parser.parse_args()

    url = _normalize_argument(args.url)

    # Use provided directory or create a temporary one
    if args.dir:
        out_dir = Path(args.dir)
        out_dir.mkdir(parents=True, exist_ok=True)
    else:
        out_dir = Path(tempfile.mkdtemp(prefix="siteshot_"))

    files = capture_screenshots(url, out_dir, viewport_height=VIEWPORT["height"])

    # Print all captured file paths newline separated
    print("\n".join(str(file) for file in files))

if __name__ == "__main__":
    main()

