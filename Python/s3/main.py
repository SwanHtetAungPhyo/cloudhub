from uploader import UploaderFactory
import argparse
# Entry point
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Upload a file to AWS S3")
    parser.add_argument("file_path", help="Local path to the file")
    parser.add_argument("bucket_name", help="S3 bucket name to upload to")
    parser.add_argument("--env", default="dev", help="Environment config key (default: dev)")

    args = parser.parse_args()

    uploader = UploaderFactory.get_uploader(env=args.env, override_bucket=args.bucket_name)
    uploader.upload_file(args.file_path)