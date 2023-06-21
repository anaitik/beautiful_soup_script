import requests
import pandas as pd

url = "https://www.ymgrad.com/api/states/"

data = []  # Store the extracted data in a list

page = 1
has_more_data = True

while has_more_data:
    # Send a GET request to the API endpoint with pagination parameters
    params = {
        "page": page
    }
    response = requests.get(url, params=params)
    json_data = response.json()

    # Extract the relevant data from the API response
    extracted_data = json_data["states_list"]

    # Add the extracted data to the list
    data.append(extracted_data)

    # Check if there is more data available
    has_more_data = json_data.get("has_more_data", False)

    # Increment the page number for the next request
    page += 1

# Flatten the JSON data
df = pd.json_normalize(data)

# Save the DataFrame to a CSV file
df.to_csv("data.csv", index=False)
