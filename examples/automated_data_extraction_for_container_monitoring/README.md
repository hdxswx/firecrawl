**Automated Data Extraction for Container Monitoring**
=====================================================

This example demonstrates how Firecrawl can be used to extract relevant data from a container monitoring platform, enabling real-time insights and automated decision-making.

**Problem**
----------

Container monitoring platforms generate vast amounts of data, making it challenging to extract relevant insights and identify potential issues. Manually processing this data is time-consuming and prone to errors.

**Technologies**
----------------

* Firecrawl
* Python
* Docker
* Container Monitoring Platform

**Output**
---------

A structured dataset containing container performance metrics, logs, and other relevant information, enabling real-time monitoring and automated decision-making.

**Example Code**
---------------

```python
import requests
import json
from firecrawl.firecrawl import FirecrawlApp

# Set your API key
api_key = "fc-YOUR_API_KEY"

# Create a FirecrawlApp instance
app = FirecrawlApp(api_key=api_key)

# Define the URL to crawl
url = "https://example.com/container-monitoring"

# Set the formats to extract
formats = ["markdown", "html"]

# Set the extraction schema (optional)
schema = {
    "type": "object",
    "properties": {
        "container_id": {"type": "string"},
        "cpu_usage": {"type": "number"},
        "memory_usage": {"type": "number"},
    },
    "required": ["container_id", "cpu_usage", "memory_usage"],
}

# Crawl the URL
response = app.crawl_url(url, params={"formats": formats, "extract": schema})

# Check if the response was successful
if response.status_code == 200:
    # Get the extracted data
    data = json.loads(response.content)

    # Extract the container ID, CPU usage, and memory usage
    container_id = data["extract"]["container_id"]
    cpu_usage = data["extract"]["cpu_usage"]
    memory_usage = data["extract"]["memory_usage"]

    # Print the extracted data
    print(f"Container ID: {container_id}")
    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory_usage}%")
else:
    print(f"Error: {response.status_code}")
```

**How to Use**
--------------

1. Set your API key in the `api_key` variable.
2. Create a FirecrawlApp instance with the API key.
3. Define the URL to crawl in the `url` variable.
4. Set the formats to extract in the `formats` variable.
5. Set the extraction schema (optional) in the `schema` variable.
6. Call the `crawl_url` method to crawl the URL and extract the data.
7. Check if the response was successful and extract the relevant data.
8. Print the extracted data.

**Benefits**
------------

* Automated data extraction from container monitoring platforms
* Real-time insights and monitoring
* Improved decision-making with structured data
* Reduced manual processing time and errors

**Limitations**
--------------

* Requires a Firecrawl API key
* Limited to extracting data from container monitoring platforms
* May require additional configuration for specific use cases