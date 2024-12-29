import pytest
import requests
from firecrawl import FirecrawlApp
from pathway import Pathway
from unittest.mock import patch, Mock

@pytest.fixture
def firecrawl_app():
    return FirecrawlApp(api_key="fc-YOUR_API_KEY")

@pytest.fixture
def pathway():
    return Pathway()

def test_scrape_url(firecrawl_app, pathway):
    url = "https://www.example.com"
    formats = ["markdown", "html"]
    response = firecrawl_app.scrape_url(url, formats=formats)
    assert response.status_code == 200
    assert response.json()["data"]["markdown"] != ""
    assert response.json()["data"]["html"] != ""

def test_generate_content(pathway):
    markdown_content = "# Hello World!"
    generated_content = pathway.generate_content(markdown_content)
    assert generated_content != ""
    assert "Hello World!" in generated_content

def test_scrape_url_with_invalid_api_key(firecrawl_app):
    firecrawl_app.api_key = "invalid_api_key"
    url = "https://www.example.com"
    formats = ["markdown", "html"]
    response = firecrawl_app.scrape_url(url, formats=formats)
    assert response.status_code == 401
    assert response.json()["error"] == "Invalid API key"

def test_generate_content_with_invalid_markdown(pathway):
    markdown_content = "Invalid markdown"
    with pytest.raises(ValueError):
        pathway.generate_content(markdown_content)

@patch("requests.Session")
def test_scrape_url_with_mocked_requests(session_mock):
    session_mock.return_value.get.return_value.json.return_value = {"data": {"markdown": "# Hello World!", "html": "<html>"}}
    firecrawl_app = FirecrawlApp(api_key="fc-YOUR_API_KEY")
    url = "https://www.example.com"
    formats = ["markdown", "html"]
    response = firecrawl_app.scrape_url(url, formats=formats)
    assert response.status_code == 200
    assert response.json()["data"]["markdown"] == "# Hello World!"
    assert response.json()["data"]["html"] == "<html>"