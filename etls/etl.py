import requests

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