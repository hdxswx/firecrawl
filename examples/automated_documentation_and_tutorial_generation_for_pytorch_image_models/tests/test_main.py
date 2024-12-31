import pytest
import os
from firecrawl import FirecrawlApp
from example import extract_model_info, generate_documentation, generate_tutorial  # Import functions from your example script


# Mock Firecrawl API key (replace with your actual key for integration tests)
os.environ["FIRECRAWL_API_KEY"] = "test_api_key"  # Or use monkeypatch fixture


@pytest.fixture
def mock_firecrawl_response(monkeypatch):
    def mock_scrape_url(self, url, params):
        if url == "https://valid_model_url.com":
            return {
                "data": {
                    "markdown": "# Mock Model Info",
                    "metadata": {"title": "Mock Model"},
                }
            }
        elif url == "https://valid_script_url.com":
            return {
                "data": {
                    "markdown": "