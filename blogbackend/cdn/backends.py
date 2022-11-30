from storages.backends.s3boto3 import S3Boto3Storage




class StaticRootS3Boto3Storage(S3Boto3Storage):
    location = 'static'
    

class MediaRootRootS3Boto3Storage(S3Boto3Storage):
    location = 'media'