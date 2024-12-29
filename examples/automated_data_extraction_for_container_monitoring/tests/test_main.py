import pytest
from firecrawl.firecrawl import FirecrawlApp
import json

@pytest.fixture
def firecrawl_app():
    api_key = "fc-YOUR_API_KEY"
    return FirecrawlApp(api_key=api_key)

def test_scrape_url(firecrawl_app):
    url = "https://example.com"
    formats = ["markdown", "html"]
    response = firecrawl_app.scrape_url(url, params={"formats": formats})
    assert response.status_code == 200
    data = json.loads(response.content)
    assert "extract" in data
    assert "markdown" in data["extract"]
    assert "html" in data["extract"]

def test_crawl_url(firecrawl_app):
    url = "https://example.com"
    formats = ["markdown", "html"]
    response = firecrawl_app.crawl_url(url, params={"formats": formats})
    assert response.status_code == 200
    data = json.loads(response.content)
    assert "extract" in data
    assert "markdown" in data["extract"]
    assert "html" in data["extract"]

def test_extract_schema(firecrawl_app):
    url = "https://example.com"
    schema = {
        "type": "object",
        "properties": {
            "title": {"type": "string"},
            "description": {"type": "string"},
        },
        "required": ["title", "description"],
    }
    response = firecrawl_app.scrape_url(url, params={"formats": ["markdown", "html"], "extract": schema})
    assert response.status_code == 200
    data = json.loads(response.content)
    assert "extract" in data
    assert "title" in data["extract"]
    assert "description" in data["extract"]

def test_scrape_url_with_schema(firecrawl_app):
    url = "https://example.com"
    schema = {
        "type": "object",
        "properties": {
            "title": {"type": "string"},
            "description": {"type": "string"},
        },
        "required": ["title", "description"],
    }
    response = firecrawl_app.scrape_url(url, params={"formats": ["markdown", "html"], "extract": schema})
    assert response.status_code == 200
    data = json.loads(response.content)
    assert "extract" in data
    assert "title" in data["extract"]
    assert "description" in data["extract"]

def test_crawl_url_with_schema(firecrawl_app):
    url = "https://example.com"
    schema = {
        "type": "object",
        "properties": {
            "title": {"type": "string"},
            "description": {"type": "string"},
        },
        "required": ["title", "description"],
    }
    response = firecrawl_app.crawl_url(url, params={"formats": ["markdown", "html"], "extract": schema})
    assert response.status_code == 200
    data = json.loads(response.content)
    assert "extract" in data
    assert "title" in data["extract"]
    assert "description" in data["extract"]