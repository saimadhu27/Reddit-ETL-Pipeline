from etls.aws_etl  import connect_to_s3, create_bucket_if_not_exists, upload_to_s3
from utils.constants import AWS_BUCKET_NAME

def upload_s3_pipeline(ti):
    file_path = ti.xcom_pull(task_ids='extract_news_data', key='return_value')
    
    if not file_path:
        raise ValueError("No file_path returned from extract_news_data via XCom")
    
    s3 = connect_to_s3()
    if s3 is None:
        raise RuntimeError("Failed to connect to S3")
    
    create_bucket_if_not_exists(s3, AWS_BUCKET_NAME)
    upload_to_s3(s3, file_path, AWS_BUCKET_NAME, file_path.split('/')[-1])
    