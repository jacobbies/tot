from apify_client import ApifyClient

# Initialize the ApifyClient with your API token
client = ApifyClient("apify_api_iLpXGuEKJ13mtrOgp3zuVGYkf8yFkZ4nGBPt")

# Prepare the Actor input
run_input = {
    "queries": "Food in NYC",
    "maxPagesPerQuery": 1,
    "resultsPerPage": 100,
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

# Run the Actor and wait for it to finish
run = client.actor("nFJndFXA5zjCTuudP").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset (if there are any)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)