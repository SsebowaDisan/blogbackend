import os



AWS_ACCESS_KEY_ID=os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY=os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME="ssebowa-cdn-backend-bucket"
AWS_S3_ENDPOINT_URL="https://nyc3.digitaloceanspaces.com"

AWS_S3_OBJECT_PARAMETERS={
    'CacheControl':"max-age=86400"
}

AWS_LOCATION = "https://ssebowa-cdn-backend-bucket.nyc3.digitaloceanspaces.com"


DEFAULT_FILE_STORAGE = "blogbackend.cdn.backends.MediaRootRootS3Boto3Storage"
STATICFILES_STORAGE = "blogbackend.cdn.backends.StaticRootS3Boto3Storage"
