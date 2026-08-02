import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from airflow import DAG
from airflow.operators.python import PythonOperator

from pipelines.news_pipeline import news_pipeline

default_args = {
    'owner': 'Madhuri',
    'start_date': datetime(2026, 8, 1)
}

file_postfix = datetime.now().strftime("%Y%m%d")

dag = DAG(
    dag_id='etl_news_pipeline',
    default_args=default_args,
    schedule='@daily',
    catchup=False,
    tags=['news', 'ETL', 'pipeline']
)

# extraction from news hacker api
extract = PythonOperator(
    task_id='extract_news_data',
    python_callable=news_pipeline,
    op_kwargs = {
        'file_name': f'news_{file_postfix}',
        'query': 'Data Engineering',
        'limit': 10
    },
    dag=dag
)

# upload to S3
# upload_s3 = PythonOperator(
#     task_id='upload_to_s3',
#     python_callable=upload_s3_pipeline,
#     dag=dag
# )

# extract >> upload_s3