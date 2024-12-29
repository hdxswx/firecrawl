import requests
import json
from firecrawl import FirecrawlApp

# Set your Firecrawl API key
API_KEY = "fc-YOUR_API_KEY"

# Create a FirecrawlApp instance
app = FirecrawlApp(api_key=API_KEY)

# Define the URL to crawl
url = "https://www.mendable.ai"

# Define the extraction schema
schema = {
    "type": "object",
    "properties": {
        "company_mission": {"type": "string"},
        "supports_sso": {"type": "boolean"},
        "is_open_source": {"type": "boolean"},
        "is_in_yc": {"type": "boolean"}
    },
    "required": ["company_mission", "supports_sso", "is_open_source", "is_in_yc"]
}

# Extract structured data from the URL
response = app.scrape_url(url, {"formats": ["extract"], "extract": {"schema": schema}})
data = response["data"]["llm_extraction"]

# Print the extracted data
print(json.dumps(data, indent=4))