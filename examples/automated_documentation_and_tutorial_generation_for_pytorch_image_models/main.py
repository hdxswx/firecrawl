import requests
from markdownify import markdownify as md
from firecrawl import FirecrawlApp
from typing import List, Dict, Any
import os

# Replace with your Firecrawl API key
FIRECRAWL_API_KEY = os.environ.get("FIRECRAWL_API_KEY")  # Retrieve from environment variables

if FIRECRAWL_API_KEY is None:
    raise ValueError("FIRECRAWL_API_KEY environment variable not set.")


def extract_model_info(url: str) -> Dict[str, Any]:
    """
    Extracts model information using Firecrawl.

    Args:
        url: The URL of the model card or documentation page.

    Returns:
        A dictionary containing the extracted information.
    """
    app = FirecrawlApp(api_key=FIRECRAWL_API_KEY)
    try:
        response = app.scrape_url(url, params={"formats": ["markdown"]})
        if response and response["data"] and response["data"]["markdown"]:
            return {"markdown": response["data"]["markdown"], "metadata": response["data"].get("metadata", {})}
        else:
            print(f"Failed to extract information from {url}. Response: {response}")
            return {}  # Return empty dictionary on failure

    except requests.exceptions.RequestException as e:
        print(f"Error during Firecrawl request: {e}")
        return {}


def generate_documentation(model_urls: List[str]) -> None:
    """
    Generates documentation for a list of PyTorch Image Models.

    Args:
        model_urls: A list of URLs pointing to model cards or documentation pages.
    """
    all_docs = []
    for url in model_urls:
        model_info = extract_model_info(url)
        if model_info:
            all_docs.append(model_info)

    # Process extracted information and generate documentation (e.g., using Markdown or other formats)
    with open("pytorch_image_models_documentation.md", "w", encoding="utf-8") as f:
        for doc in all_docs:
            f.write(f"# {doc['metadata'].get('title', 'Untitled')}\n\n")
            f.write(doc["markdown"])
            f.write("\n\n---\n\n")  # Separator between model entries

    print("Documentation generated successfully!")


def generate_tutorial(model_url: str, example_script_url: str) -> None:
    """
    Generates an interactive tutorial for a specific model.

    Args:
        model_url: The URL of the model card or documentation page.
        example_script_url: The URL of an example script demonstrating the model's usage.
    """

    model_info = extract_model_info(model_url)
    example_code = extract_model_info(example_script_url) # Extract code as markdown


    if model_info and example_code:
        with open("pytorch_model_tutorial.md", "w", encoding="utf-8") as f:
            f.write(f"# Tutorial: {model_info['metadata'].get('title', 'Untitled')}\n\n")
            f.write(model_info["markdown"])  # Include model description
            f.write("\n\n## Example Code:\n\n")
            f.write("