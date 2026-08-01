import os
import sys
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

default_args = {
    'owner': 'Madhuri',
    'start_date': datetime(2026, 08, 01)
}

file_postfix = datetime.now().strftime("%Y%m%d")

dag = DAG(
    dag_id='etl_reddit_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=['reddit', 'ETL', 'pipeline']
)

# extraction from reddit
extract = PythonOperator(
    task_id='extract_reddit_data',
    python_callable=reddit_pipeline,
    op_kwargs = {
        'file_name': f'reddit_{file_postfix}',
        'subreddit': 'dataengineering',
        'time_filter': 'day',
        'limit': 100
    },
    dag=dag
)

# upload to S3
upload_s3 = PythonOperator(
    task_id='upload_to_s3',
    python_callable=upload_s3_pipeline,
    dag=dag
)

extract >> upload_s3