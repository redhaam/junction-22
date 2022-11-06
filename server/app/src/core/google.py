from google.cloud import storage
import datetime, os
from fastapi import UploadFile
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = f"{os.getcwd()}/creds.json"
storage_client = storage.Client()


def upload_file(bucket_name:str,file: UploadFile, filename:str  ):  
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(filename if filename is not None else file.filename)
    blob.upload_from_file(file.file, content_type= file.content_type)
    url = blob.generate_signed_url(expiration=datetime.timedelta(days=365))
    return url