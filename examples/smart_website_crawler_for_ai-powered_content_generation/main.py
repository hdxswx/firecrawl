import requests
import json
from firecrawl import FirecrawlApp
from pathway import Pathway

# Set your Firecrawl API key
firecrawl_api_key = "fc-YOUR_API_KEY"

# Set the URL to extract data from
url = "https://www.example.com"

# Create a FirecrawlApp instance
firecrawl_app = FirecrawlApp(api_key=firecrawl_api_key)

# Extract data from the website using Firecrawl
response = firecrawl_app.scrape_url(url, formats=["markdown", "html"])

# Extract the markdown content from the response
markdown_content = response["data"]["markdown"]

# Create a Pathway instance
pathway = Pathway()

# Use Pathway to generate AI-powered content from the markdown content
generated_content = pathway.generate_content(markdown_content)

# Print the generated content
print(generated_content)