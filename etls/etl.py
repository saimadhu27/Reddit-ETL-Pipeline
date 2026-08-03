import requests
import pandas as pd

def search_hn(query, limit=10):
    """Returns a lit of dicts according to the search term

    Args:
        query (str): search term eg. data engineering
        limit (int, optional): no of results. Defaults to 10.

    Returns:
        _type_: A list of dicts
    """
    url = "https://hn.algolia.com/api/v1/search_by_date"
    params = {"query": f'"{query}"', "tags": "story", "hitsPerPage": limit}
    response = requests.get(url, params=params)
    return response.json()["hits"]

def extract_data(search_results):
    """Extract the required fields from the result

    Args:
        search_results (instance): instance of the search_hn function

    Returns:
        _type_: A list of dicts with the required fields
    """
    extracted_data = []
    for result in search_results:
        extracted_data.append({
            "object_id": result.get("objectID"),
            "story_id": result.get("story_id"),
            "title": result.get("title"),
            "author": result.get("author"),
            "created_at": result.get("created_at"),
            "num_comments": result.get("num_comments"),
            "points": result.get("points"),
            "updated_at": result.get("updated_at"),
            "url": result.get("url")
        })
    return extracted_data 

def transform_data(news_df: pd.DataFrame):
    news_df['created_at'] = pd.to_datetime(news_df['created_at'])
    news_df['updated_at'] = pd.to_datetime(news_df['updated_at'])
    return news_df

def load_data_to_csv(data: pd.DataFrame, path: str):
    data.to_csv(path, index=False)