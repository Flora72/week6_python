import requests
import os
import hashlib
from urllib.parse import urlparse
from datetime import datetime

def sanitize_filename(filename):
    return filename.replace("?", "_").replace("&", "_").replace("=", "_")

def generate_filename(url):
    parsed_url = urlparse(url)
    base = os.path.basename(parsed_url.path)
    if base:
        return sanitize_filename(base)
    # Fallback: generate hash-based name
    hash_name = hashlib.md5(url.encode()).hexdigest()
    return f"image_{hash_name}.jpg"

def already_downloaded(filepath):
    return os.path.exists(filepath)

def fetch_image(url, folder="Fetched_Images"):
    try:
        os.makedirs(folder, exist_ok=True)

        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Check content type
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"✗ Skipped: URL does not point to an image ({content_type})")
            return

        filename = generate_filename(url)
        filepath = os.path.join(folder, filename)

        if already_downloaded(filepath):
            print(f"✓ Already exists: {filename}")
            return

        with open(filepath, 'wb') as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An error occurred: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    urls = input("Please enter image URLs (comma-separated): ").split(',')

    for url in urls:
        url = url.strip()
        if url:
            fetch_image(url)

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
