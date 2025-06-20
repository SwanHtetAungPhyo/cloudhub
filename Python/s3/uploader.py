import logging
import os
import boto3
from abc import ABC, abstractmethod
from botocore.exceptions import ClientError

from config import CONFIG

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

# Abstract base class
class CloudStorageHandler(ABC):
    @abstractmethod
    def upload_file(self, file_path: str, key: str = None) -> None:
        pass

    @abstractmethod
    def download_file(self, file_path: str, key: str = None) -> None:
        pass

# Concrete S3 uploader
class S3Uploader(CloudStorageHandler):
    def __init__(self, aws_access_key, aws_secret_key, bucket_name, region):
        self.bucket_name = bucket_name
        self.client = boto3.client(
            "s3",
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key,
            region_name=region
        )
        logging.info(f"S3Uploader initialized for bucket: {bucket_name}")

    def upload_file(self, file_path: str, key: str = None) -> None:
        if not key:
            key = os.path.basename(file_path)

        try:
            self.client.upload_file(file_path, self.bucket_name, key)
            logging.info(f"✅ Uploaded '{file_path}' as '{key}' to bucket '{self.bucket_name}'")
        except Exception as e:
            logging.error(f"❌ Upload failed: {e}")

    def download_file(self, file_path: str, key: str = None) -> None:
        if not key:
            key = os.path.basename(file_path)

        try:
            self.client.download_file(self.bucket_name, key, file_path)
            logging.info(f"✅ Downloaded '{key}' to '{file_path}'")
        except ClientError as e:
            logging.error(f"❌ Download failed: {e}")

# Factory pattern for uploader
class UploaderFactory:
    @staticmethod
    def get_uploader(env: str, override_bucket: str = None) -> CloudStorageHandler:
        if env not in CONFIG:
            raise ValueError(f"Unknown environment '{env}'")
        cfg = CONFIG[env]

        bucket = override_bucket if override_bucket else cfg["bucket_name"]

        return S3Uploader(
            aws_access_key=cfg["aws_access_key_id"],
            aws_secret_key=cfg["aws_secret_access_key"],
            bucket_name=bucket,
            region=cfg["region_name"]
        )


