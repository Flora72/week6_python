# Library importation
# These libraries help with HTTP requests, file handling, URL parsing, and timestamping.
import requests
import os
import hashlib
from urllib.parse import urlparse
from datetime import datetime

# Sanitize filenames to avoid problematic characters
def sanitize_filename(filename):
    return filename.replace("?", "_").replace("&", "_").replace("=", "_")

# Generate a safe, unique filename from the image URL
def generate_filename(url):
    parsed_url = urlparse(url)
    base = os.path.basename(parsed_url.path)
    if base:
        return sanitize_filename(base)
    # If no basename is found, fallback to a hash-based name for uniqueness
    hash_name = hashlib.md5(url.encode()).hexdigest()
    return f"image_{hash_name}.jpg"

# Check if the image has already been downloaded
def already_downloaded(filepath):
    return os.path.exists(filepath)

# Fetch and save the image from the web
def fetch_image(url, folder="Fetched_Images"):
    try:
        # Create the folder if it doesn't exist
        os.makedirs(folder, exist_ok=True)

        # Send a GET request to the image URL
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Validate that the response is an image
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"✗ Skipped: URL does not point to an image ({content_type})")
            return

        # Generate a filename and full path
        filename = generate_filename(url)
        filepath = os.path.join(folder, filename)

        # Avoid re-downloading if the image already exists
        if already_downloaded(filepath):
            print(f"✓ Already exists: {filename}")
            return

        # Save the image content to disk
        with open(filepath, 'wb') as f:
            f.write(response.content)

        # Confirm success
        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    # Handle connection-related errors gracefully
    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    # Catch any other unexpected issues
    except Exception as e:
        print(f"✗ An error occurred: {e}")

# Entry point for the tool
def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Prompt user for comma-separated image URLs
    urls = input("Please enter image URLs (comma-separated): ").split(',')

    # Process each URL individually
    for url in urls:
        url = url.strip()
        if url:
            fetch_image(url)

    print("\nConnection strengthened. Community enriched.")

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
