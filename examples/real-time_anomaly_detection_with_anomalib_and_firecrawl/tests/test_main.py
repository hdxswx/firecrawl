import pytest
from firecrawl import FirecrawlApp
import json

@pytest.fixture
def firecrawl_app():
    api_key = "fc-YOUR_API_KEY"
    return FirecrawlApp(api_key=api_key)

def test_scrape_url(firecrawl_app):
    url = "https://www.mendable.ai"
    response = firecrawl_app.scrape_url(url, {"formats": ["markdown", "html"]})
    assert response.status_code == 200
    data = response.json()
    assert "content" in data
    assert "metadata" in data
    assert "llm_extraction" in data

def test_crawl_url(firecrawl_app):
    url = "https://www.mendable.ai"
    response = firecrawl_app.crawl_url(url, {"limit": 100, "scrapeOptions": {"formats": ["markdown", "html"]}})
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert "total" in data
    assert "creditsUsed" in data

def test_extract_schema(firecrawl_app):
    url = "https://www.mendable.ai"
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
    response = firecrawl_app.scrape_url(url, {"formats": ["extract"], "extract": {"schema": schema}})
    data = response.json()
    assert "llm_extraction" in data
    extracted_data = data["llm_extraction"]
    assert "company_mission" in extracted_data
    assert "supports_sso" in extracted_data
    assert "is_open_source" in extracted_data
    assert "is_in_yc" in extracted_data

def test_batch_scrape(firecrawl_app):
    urls = ["https://www.mendable.ai", "https://www.mendable.ai/sdks/overview"]
    response = firecrawl_app.batch_scrape(urls, {"formats": ["markdown", "html"]})
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert len(data["data"]) == 2

def test_search(firecrawl_app):
    query = "firecrawl"
    response = firecrawl_app.search(query, {"pageOptions": {"fetchPageContent": True}})
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert len(data["data"]) > 0