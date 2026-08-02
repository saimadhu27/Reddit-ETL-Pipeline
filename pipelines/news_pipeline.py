import pandas as pd
from etls.etl import search_hn, extract_data

def news_pipeline(file_name: str, query:str, limit=10):
    # connecting to news hacker api 
    search_results = search_hn(query, limit)
    # extracting data from news hacker api
    extracted_data = extract_data(search_results)
    # transformation
    
    # loading data to csv