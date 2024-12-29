import requests
import json
from firecrawl.firecrawl import FirecrawlApp

# Set your API key
api_key = "fc-YOUR_API_KEY"

# Create a FirecrawlApp instance
app = FirecrawlApp(api_key=api_key)

# Define the URL to crawl
url = "https://docs.firecrawl.dev"

# Define the formats to extract
formats = ["markdown", "html"]

# Crawl the URL
crawl_status = app.crawl_url(url, params={"limit": 100, "scrapeOptions": {"formats": formats}})

# Check if the crawl was successful
if crawl_status["status"] == "success":
    # Get the extracted data
    data = crawl_status["data"]

    # Print the extracted data
    print("Extracted data:")
    print(json.dumps(data, indent=4))

    # Extract structured data using LLM extraction
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

    extraction_options = {"schema": schema}
    extraction_result = app.scrape_url(url, params={"formats": ["extract"], "extract": extraction_options})

    if extraction_result:
        print("Extracted structured data:")
        print(json.dumps(extraction_result["extract"], indent=4))

else:
    print("Crawl failed:", crawl_status["message"])