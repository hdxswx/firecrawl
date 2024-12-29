import pytest
from firecrawl.firecrawl import FirecrawlApp
from firecrawl.exceptions import FirecrawlException

@pytest.fixture
def firecrawl_app():
    api_key = "fc-YOUR_API_KEY"
    return FirecrawlApp(api_key=api_key)

def test_crawl_url(firecrawl_app):
    url = "https://docs.firecrawl.dev"
    formats = ["markdown", "html"]
    params = {"limit": 100, "scrapeOptions": {"formats": formats}}
    response = firecrawl_app.crawl_url(url, params=params)
    assert response["status"] == "success"

def test_extract_structured_data(firecrawl_app):
    url = "https://docs.firecrawl.dev"
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
    response = firecrawl_app.scrape_url(url, params={"formats": ["extract"], "extract": extraction_options})
    assert response["extract"]

def test_invalid_api_key(firecrawl_app):
    firecrawl_app.api_key = "invalid_api_key"
    with pytest.raises(FirecrawlException):
        firecrawl_app.crawl_url("https://docs.firecrawl.dev")

def test_missing_api_key(firecrawl_app):
    firecrawl_app.api_key = None
    with pytest.raises(FirecrawlException):
        firecrawl_app.crawl_url("https://docs.firecrawl.dev")

def test_invalid_url(firecrawl_app):
    url = "invalid_url"
    with pytest.raises(FirecrawlException):
        firecrawl_app.crawl_url(url)

def test_invalid_formats(firecrawl_app):
    url = "https://docs.firecrawl.dev"
    formats = ["invalid_format"]
    params = {"limit": 100, "scrapeOptions": {"formats": formats}}
    with pytest.raises(FirecrawlException):
        firecrawl_app.crawl_url(url, params=params)

def test_missing_formats(firecrawl_app):
    url = "https://docs.firecrawl.dev"
    params = {"limit": 100}
    with pytest.raises(FirecrawlException):
        firecrawl_app.crawl_url(url, params=params)