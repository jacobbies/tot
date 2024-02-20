from apify_client import ApifyClient
from dotenv import load_dotenv
import os
import requests

# Load .env variables and initialize apifyclient with API token
load_dotenv()
APIFY_API_KEY = os.getenv('APIFY_API_KEY')
client = ApifyClient(APIFY_API_KEY)

user_query = input("Enter your query: ")

# Prepare Actor input
run_input = {
    "queries": user_query,
    "maxPagesPerQuery": 1,
    "resultsPerPage": 5,
    "mobileResults": False,
    "languageCode": "",
    "maxConcurrency": 10,
    "saveHtml": False,
    "saveHtmlToKeyValueStore": False,
    "includeUnfilteredResults": False,
    "customDataFunction": """async ({ input, $, request, response, html }) => {
  return {
    pageTitle: $('title').text(),
  };
};""",
}

# Run Actor
run = client.actor("nFJndFXA5zjCTuudP").call(run_input=run_input)

# Fetch and print Actor results from run's dataset (if there are any)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)