**Real-time Anomaly Detection with Anomalib and Firecrawl**
=====================================================

Anomalib is an anomaly detection library that provides state-of-the-art algorithms and features. This example demonstrates how to use Firecrawl to extract relevant data from web sources and feed it into Anomalib for real-time anomaly detection.

**Problem:**
Detecting anomalies in real-time data streams from various sources, such as IoT devices or financial transactions, is a challenging task. Anomalib provides a robust solution, but it requires structured data as input. Firecrawl helps bridge this gap by extracting relevant data from web sources and converting it into a format suitable for Anomalib.

**Technologies:**
Anomalib, Firecrawl, Python, web scraping, machine learning

**Output:**
Real-time anomaly detection results, including alerts and visualizations, using Anomalib's API and Firecrawl's extracted data

**Firecrawl Readme:**
```
{"message":"Not Found","documentation_url":"https://docs.github.com/rest","status":"404"}
```

**Inspiration Repository Readme:**
```
<h3 align="center">
  <a name="readme-top"></a>
  <img
    src="https://raw.githubusercontent.com/mendableai/firecrawl/main/img/firecrawl_logo.png"
    height="200"
  >
</h3>
<div align="center">
    <a href="https://github.com/mendableai/firecrawl/blob/main/LICENSE">
  <img src="https://img.shields.io/github/license/mendableai/firecrawl" alt="License">
</a>
    <a href="https://pepy.tech/project/firecrawl-py">
  <img src="https://static.pepy.tech/badge/firecrawl-py" alt="Downloads">
</a>
<a href="https://GitHub.com/mendableai/firecrawl/graphs/contributors">
  <img src="https://img.shields.io/github/contributors/mendableai/firecrawl.svg" alt="GitHub Contributors">
</a>
<a href="https://firecrawl.dev">
  <img src="https://img.shields.io/badge/Visit-firecrawl.dev-orange" alt="Visit firecrawl.dev">
</a>
</div>
<div>
  <p align="center">
    <a href="https://twitter.com/firecrawl_dev">
      <img src="https://img.shields.io/badge/Follow%20on%20X-000000?style=for-the-badge&logo=x&logoColor=white" alt="Follow on X" />
    </a>
    <a href="https://www.linkedin.com/company/104100957">
      <img src="https://img.shields.io/badge/Follow%20on%20LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Follow on LinkedIn" />
    </a>
    <a href="https://discord.com/invite/gSmWdAkdwd">
      <img src="https://img.shields.io/badge/Join%20our%20Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Join our Discord" />
    </a>
  </p>
</div>
```

**Features:**
- **Scrape**: scrapes a URL and get its content in LLM-ready format (markdown, structured data via [LLM Extraction](#llm-extraction-beta), screenshot, html)
- **Crawl**: scrapes all the URLs of a web page and return content in LLM-ready format
- **Map** (Alpha): input a website and get all the website urls - extremely fast

**Powerful Capabilities:**
- **LLM-ready formats**: markdown, structured data, screenshot, HTML, links, metadata
- **The hard stuff**: proxies, anti-bot mechanisms, dynamic content (js-rendered), output parsing, orchestration
- **Customizability**: exclude tags, crawl behind auth walls with custom headers, max crawl depth, etc...
- **Media parsing**: pdfs, docx, images
- **Reliability first**: designed to get the data you need - no matter how hard it is
- **Actions**: click, scroll, input, wait and more before extracting data
- **Batching (New)**: scrape thousands of URLs at the same time with a new async endpoint.

**Crawling:**
Used to crawl a URL and all accessible subpages. This submits a crawl job and returns a job ID to check the status of the crawl.

```bash
curl -X POST https://api.firecrawl.dev/v1/crawl \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer fc-YOUR_API_KEY' \
    -d '{
      "url": "https://docs.firecrawl.dev",
      "limit": 100,
      "scrapeOptions": {
        "formats": ["markdown", "html"]
      }
    }'
```

**Scraping:**
Used to scrape a URL and get its content in the specified formats.

```bash
curl -X POST https://api.firecrawl.dev/v1/scrape \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -d '{
      "url": "https://docs.firecrawl.dev",
      "formats" : ["markdown", "html"]
    }'
```

**LLM Extraction (Beta):**
Used to extract structured data from scraped pages.

```bash
curl -X POST https://api.firecrawl.dev/v1/scrape \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -d '{
      "url": "https://www.mendable.ai/",
      "formats": ["extract"],
      "extract": {
        "schema": {
          "type": "object",
          "properties": {
            "company_mission": {
              "type": "string"
            },
            "supports_sso": {
              "type": "boolean"
            },
            "is_open_source": {
              "type": "boolean"
            },
            "is_in_yc": {
              "type": "boolean"
            }
          },
          "required": [
            "company_mission",
            "supports_sso",
            "is_open_source",
            "is_in_yc"
          ]
        }
      }
    }'
```

**Using Python SDK:**
```python
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
```

**Using the Node SDK:**
```javascript
import { FirecrawlApp } from '@mendable/firecrawl-js';

const app = new FirecrawlApp({ apiKey: 'fc-YOUR_API_KEY' });

// Define the URL to crawl
const url = 'https://www.mendable.ai';

// Define the extraction schema
const schema = {
  type: 'object',
  properties: {
    company_mission: { type: 'string' },
    supports_sso: { type: 'boolean' },
    is_open_source: { type: 'boolean' },
    is_in_yc: { type: 'boolean' }
  },
  required: ['company_mission', 'supports_sso', 'is_open_source', 'is_in_yc']
};

// Extract structured data from the URL
const response = await app.scrapeUrl(url, { formats: ['extract'], extract: { schema } });
const data = response.data.llm_extraction;

// Print the extracted data
console.log(JSON.stringify(data, null, 4));
```

**Open Source vs Cloud Offering:**
Firecrawl is open source available under the AGPL-3.0 license. To deliver the best possible product, we offer a hosted version of Firecrawl alongside our open-source offering. The cloud solution allows us to continuously innovate and maintain a high-quality, sustainable service for all users.

**Contributing:**
We love contributions! Please read our [contributing guide](CONTRIBUTING.md) before submitting a pull request. If you'd like to self-host, refer to the [self-hosting guide](SELF_HOST.md).

**License Disclaimer:**
This project is primarily licensed under the GNU Affero General Public License v3.0 (AGPL-3.0), as specified in the LICENSE file in the root directory of this repository. However, certain components of this project are licensed under the MIT License. Refer to the LICENSE files in these specific directories for details.