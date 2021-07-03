import requests
import json

HeadersType = dict[str, str]


def retrieveDatabase(
        databaseId: str,
        headers: HeadersType,
        query: dict = {},
        save_to_json: bool = False) -> dict:

    # Construct database url
    base_url = "https://api.notion.com/v1/databases/"
    url = base_url + databaseId + "/query"

    # POST
    response = requests.post(url=url, headers=headers, json=query)
    print(response.headers['content-type'])
    if response.status_code == 200:
        database = response.json()

        if save_to_json:
            with open("./daily-email/saved-data/database.json", "w", encoding="utf8") as f:
                json.dump(database, f, ensure_ascii=False)

        return database
    else:
        print(f"Error {response.status_code} with:")
        print(f"Url: {url}")
        print(f"Headers: {headers}")
        print(f"Query: {query}")
        return dict()
