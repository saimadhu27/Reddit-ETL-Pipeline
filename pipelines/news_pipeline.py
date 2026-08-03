import os
import pandas as pd
from etls.etl import *
from utils.constants import OUTPUT_PATH

def news_pipeline(file_name: str, query:str, limit=10):
    # connecting to news hacker api
    search_results = search_hn(query, limit)
    # extracting data from news hacker api
    extracted_data = extract_data(search_results)
    news_df = pd.DataFrame(extracted_data)
    # transformation
    news_df = transform_data(news_df)
    # loading data to csv
    output_file = os.path.join(OUTPUT_PATH, f'{file_name}.csv')
    load_data_to_csv(news_df, output_file)