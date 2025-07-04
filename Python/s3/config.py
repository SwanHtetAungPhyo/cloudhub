import os
import  dotenv

dotenv.load_dotenv()

CONFIG = {
    "dev": {
        "aws_access_key_id": os.getenv("AWS_ACCESS_KEY_ID"),
        "aws_secret_access_key": os.getenv("AWS_SECRET_ACCESS_KEY"),
        "region_name": os.getenv("AWS_REGION_NAME"),
        "bucket_name": os.getenv("BUCKET_NAME"),
    }
}