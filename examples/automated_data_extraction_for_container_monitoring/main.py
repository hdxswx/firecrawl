import requests
import json
from firecrawl.firecrawl import FirecrawlApp

# Set your API key
api_key = "fc-YOUR_API_KEY"

# Create a FirecrawlApp instance
app = FirecrawlApp(api_key=api_key)

# Define the URL to crawl
url = "https://example.com"

# Set the formats to extract
formats = ["markdown", "html"]

# Set the extraction schema (optional)
schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "description": {"type": "string"},
    },
    "required": ["title", "description"],
}

# Crawl the URL
response = app.crawl_url(url, params={"formats": formats, "extract": schema})

# Check if the response was successful
if response.status_code == 200:
    # Get the extracted data
    data = json.loads(response.content)

    # Extract the title and description
    title = data["extract"]["title"]
    description = data["extract"]["description"]

    # Print the extracted data
    print(f"Title: {title}")
    print(f"Description: {description}")
else:
    print(f"Error: {response.status_code}")